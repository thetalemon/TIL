<template>
  <div class="hello">
    <h1>Hello {{ login_username }}!!</h1>

    <button v-if="login_username==''" @click="show_modal('signin_modal')">サインインする</button>
    <modal name="signin_modal" :adaptive="true" width="80%" height="80%">
      <h2>Sign in</h2>
      <input type="text" placeholder="Username" v-model="input_username">
      <input type="password" placeholder="Password" v-model="input_password">
      <button @click="signIn">サインインする</button>
      <button @click="signUp">アカウントを作る</button>
      <p><button @click="hide_modal('signin_modal')">hide</button></p>
    </modal>

    <button v-if="login_username!=''" @click="signOut">サインアウトする</button>

    <!-- 投稿フォーム -->
    <button v-if="login_username!=''" @click="show_modal('submit_modal')">投稿する</button>
    <modal name="submit_modal" :adaptive="true"  width="80%" height="80%">
      <p><canvas ref="canvas" class="resize-img__preview__canvas"/></p>
      <p><input type="file" @change="onFileChange"></p>
      <p><button @click="hide_modal('submit_modal')">hide</button></p>
    </modal>

    <!-- 投稿一覧 -->
    <ul  class="box-list">
      <li v-for="(comment,key, index) in comments" :key="index">
        <div><img class="top" :src="comment.content" @click="show_img(key)"></div>
        <modal name="img_modal" :adaptive="true"  width="80%" height="80%">
          <p><img :src="modal_img"></p>
          <p>{{modal_createdAt}}</p>
          <p><button @click="hide_modal('img_modal')">hide</button></p>
        </modal>
      </li>
    </ul>

  </div>
</template>

<script>
import axios from 'axios'
import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/firestore'
import 'firebase/storage'

export default {
  name: 'HelloWorld',
  data: () => ({
    name: '',
    comments: [],
    modal_img: '',
    modal_createdAt: '',
    input_username: '',
    input_password: '',
    login_username: '',
    labels: []
  }),
  methods: {
    signIn: function () {
      firebase.auth().signInWithEmailAndPassword(this.input_username, this.input_password)
        .then(user => {
          this.login_username = firebase.auth().currentUser.email
          this.$modal.hide('signin_modal')
        },
        err => {
          alert(err.message)
        })
    },
    signUp: function () {
      firebase.auth().createUserWithEmailAndPassword(this.input_username, this.input_password)
      firebase.auth().signInWithEmailAndPassword(this.input_username, this.input_password)
        .then(user => {
          this.login_username = firebase.auth().currentUser.email
          this.$modal.hide('signin_modal')
        })
        .catch(error => {
          alert(error.message)
        })
    },
    signOut: function () {
      firebase.auth().signOut()
        .then(user => {
          this.login_username = ''
        })
        .catch(error => {
          alert(error.message)
        })
    },
    onFileChange (e) {
      e.preventDefault()

      var file = e.target.files[0]
      const reader = new FileReader()
      reader.onload = (e) => {
        this.insertImg(e.target.result)
      }
      reader.readAsDataURL(file)
    },
    insertImg (file) {
      const image = new Image()
      image.crossOrigin = 'Anonymous'
      image.onload = (e) => {
        // リサイズ
        const resizedBase64 = this.makeResizeImg(image)
        // 現在時刻
        let timestamp = firebase.firestore.FieldValue.serverTimestamp()
        // this.insertStorage(resizedBase64)
        this.post2VisionApi(resizedBase64)
        // DBへINSERT
        firebase.firestore().collection('picts').add({
          content: resizedBase64,
          uid: firebase.auth().currentUser.uid,
          createdAt: timestamp
        })
        // 投稿一覧へ追加
        this.comments.unshift({
          content: resizedBase64,
          createdAt: timestamp
        })
      }
      image.src = file
    },
    insertStorage (img) {
      var storageRef = firebase.storage().ref().child('mountains.jpg')
      // storageRef.putString(resizedBase64, 'data_url').then(function (snapshot) {
      //   console.log('Uploaded a base64url string!')
      // })
      console.log('a')

      storageRef.getDownloadURL()
        .then(url => {
          console.log(url)
        })
    },
    paramsSerializer (param) {
      const qs = require('qs')

      return qs.stringify(param, {arrayFormat: 'brackets'})
    },
    post2VisionApi (image) {
      var str = image.replace('data:image/png;base64,', '')
      const config = require('../config.js')
      console.log(str)

      // let params = new URLSearchParams()
      // params.append('text', 'テストだよー');
      // console.log('b')
      // var param = {
      //   // key: config.apiKey,
      //   requests: [
      //     {
      //       image: {
      //         content: str
      //       },
      //       features: [
      //         {
      //           type: 'LABEL_DETECTION',
      //           maxResults: 3
      //         }
      //       ]
      //     }
      //   ]
      // }
      var param = {
        image: {
          content: str
        },
        features: [
          {
            type: 'LABEL_DETECTION',
            maxResults: 3
          }
        ]
      }
      console.log(param)

      // axios.post('https://vision.googleapis.com/v1/images:annotate?key=' + config.apiKey, param)

      let request = new URLSearchParams()
      request.append('key', config.apiKey)
      // request.append('requests', this.paramsSerializer(param))
      axios.post('https://vision.googleapis.com/v1/images:annotate', request, param)
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    makeResizeImg (image) {
      // リサイズするメソッド
      const canvas = this.$refs.canvas
      const ctx = canvas.getContext('2d')
      const MAX_SIZE = 500
      let width = image.width
      let height = image.height

      if (width < MAX_SIZE && height < MAX_SIZE) {
        // MAX_SIZEよりも小さいならばそのまま
        [canvas.width, canvas.height] = [width, height]
      } else if (image.width > image.height) {
        // ヨコ＞タテならば、ヨコが500になるようにリサイズ
        [canvas.width, canvas.height] = [MAX_SIZE, ((height * MAX_SIZE) / width)]
      } else {
        // タテ＞ヨコならば、タテが500になるようにリサイズ
        [canvas.width, canvas.height] = [((width * MAX_SIZE) / height), MAX_SIZE]
      }
      ctx.drawImage(image, 0, 0, width, height, 0, 0, canvas.width, canvas.height)
      return canvas.toDataURL('image/png')
    },
    show_modal: function (modalName) {
      this.$modal.show(modalName)
    },
    hide_modal: function (modalName) {
      this.$modal.hide(modalName)
    },
    show_img: function (key) {
      this.$modal.show('img_modal')
      // モーダル内の画像を対象画像に差し替える
      this.modal_img = this.comments[key].content
      this.modal_createdAt = this.comments[key].createdAt
    }
  },
  created: function () {
    // firebase.firestore().collection('picts').orderBy('createdAt', 'desc').get()
    //   .then((snapshot) => {
    //     snapshot.forEach((doc) => {
    //       console.log(doc.id, '=>', doc.data())
    //       this.comments.push({
    //         content: doc.data().content,
    //         createdAt: doc.data().createdAt.toDate().toLocaleString()
    //       })
    //     })
    //   })
    //   .catch((err) => {
    //     console.log('Error getting documents', err)
    //   })
  }
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
.hello{
 text-align: center;
}
table{
  border: 2px #2b2b2b solid;
}
img {
  margin: 10px;
}
img.top {
  width: 250px;
  height: 250px;
  object-fit: cover;
}
p{
  text-align: center;
}
.box-list{
  display: flex;
  margin: 0px;
  padding: 0px;
  list-style: none;
  flex-flow: row wrap;
}
.box-list li{
  flex: 0 0 10%;
  margin-bottom: 0px;
}
</style>
