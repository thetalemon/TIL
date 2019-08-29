<template>
  <div class="hello">
    <!-- サインイン・サインアウト -->
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

    <!-- タグクラウド -->
    <button @click="show_modal('tag_cloud')">タグ一覧</button>
    <modal name="tag_cloud" :adaptive="true"  width="80%" height="80%">
      <ul>
        <p><button @click="hide_modal('tag_cloud')">hide</button></p>
        <a v-for="(tag, key, index) in tags" :key="index" @click="get_tag_images(tag.tagName)">{{tag.tagName}}({{tag.count}}), </a>
      </ul>
    </modal>

    <!-- 投稿フォーム -->
    <button v-if="login_username!=''" @click="show_modal('submit_modal')">投稿する</button>
    <modal name="submit_modal" :adaptive="true"  width="80%" height="80%">
      <p><canvas ref="canvas" class="resize-img__preview__canvas"/></p>
      <p><input type="file" @change="onFileChange"></p>
      <p><button @click="hide_modal('submit_modal')">hide</button></p>
    </modal>

    <!-- 投稿一覧 -->
    <ul  class="box-list">
      <li v-for="(pict, key, index) in picts" :key="index">
        <div><img class="top" :src="pict.content" @click="show_img(key)"></div>
        <modal name="img_modal" :adaptive="true"  width="80%" height="80%">
          <p><img :src="modal_content.pict"></p>
          <p><a @click="get_tag_images(modal_content.tag1)">{{modal_content.tag1}}</a></p>
          <p><a @click="get_tag_images(modal_content.tag2)">{{modal_content.tag2}}</a></p>
          <p><a @click="get_tag_images(modal_content.tag3)">{{modal_content.tag3}}</a></p>
          <p>{{modal_content.time}}</p>
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
    picts: [],
    tags: [],
    all_picts: [],
    modal_content: [],
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
        this.setImg(e.target.result)
      }
      reader.readAsDataURL(file)
    },
    setImg (file) {
      const image = new Image()
      image.crossOrigin = 'Anonymous'
      image.onload = (e) => {
        // リサイズ
        const resizedBase64 = this.makeResizeImg(image)

        // 現在時刻
        let timestamp = firebase.firestore.FieldValue.serverTimestamp()

        // DBへINSERT
        this.insertImg(resizedBase64, timestamp)

        this.$modal.hide('submit_modal')
      }
      image.src = file
    },
    insertImg (image, timestamp) {
      var str = image.replace('data:image/png;base64,', '')
      var param = {
        requests: [
          {
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
        ]
      }

      const config = require('../config.js')
      axios({
        method: 'post',
        url: 'https://vision.googleapis.com/v1/images:annotate?key=' + config.apiKey,
        data: param,
        config: {
          headers: {
            'Content-Type': 'application/json'
          }
        }
      }).then((response) => {
        const tags = [
          response.data.responses[0].labelAnnotations[0].description,
          response.data.responses[0].labelAnnotations[1].description,
          response.data.responses[0].labelAnnotations[2].description
        ]

        // 画像データのINSERT
        firebase.firestore().collection('picts').add({
          content: image,
          uid: firebase.auth().currentUser.uid,
          createdAt: timestamp,
          tag1: tags[0],
          tag2: tags[1],
          tag3: tags[2]
        })

        // タグデータのINSERT
        for (let i = 0; i < 3; i++) {
          console.log(tags[i])
          firebase.firestore().collection('tags').doc(tags[i]).get()
            .then(doc => {
              if (!doc.exists) {
                // 対象タグが初のとき：登録
                firebase.firestore().collection('tags').doc(tags[i]).set({
                  count: 1
                })
              } else {
                // 対象タグがすでにあるとき：加算
                let countUp = doc.data().count + 1
                firebase.firestore().collection('tags').doc(tags[i]).set({
                  count: countUp
                })
              }
            })
            .catch(err => {
              console.log('Error getting document', err)
            })
        }

        // 投稿一覧へ追加
        this.picts.unshift({
          content: image,
          // 本当は時間も載せないといけないが、timestampが決定されるのがデータがfirestoreに挿入される時点なので、
          // 時間を取得するには、1回Selectする必要がある。が、負荷かけるほど大事な情報でもないので、一旦割愛する。
          // createdAt: timestamp,
          tag1: tags[0],
          tag2: tags[1],
          tag3: tags[2]
        })
      }).catch(function (error) {
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
      this.modal_content = {
        pict: this.picts[key].content,
        time: this.picts[key].createdAt,
        tag1: this.picts[key].tag1,
        tag2: this.picts[key].tag2,
        tag3: this.picts[key].tag3
      }
    },
    get_tag_images: function (tagName) {
      this.picts = this.all_picts.filter(function (value) {
        if (value.tag1 === tagName) {
          return true
        } else if (value.tag2 === tagName) {
          return true
        } else if (value.tag3 === tagName) {
          return true
        } else {
          return false
        }
      })
    }
  },
  created: function () {
    firebase.firestore().collection('picts').orderBy('createdAt', 'desc').get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          console.log(doc.id, '=>', doc.data())
          this.picts.push({
            content: doc.data().content,
            createdAt: doc.data().createdAt.toDate().toLocaleString(),
            tag1: doc.data().tag1,
            tag2: doc.data().tag2,
            tag3: doc.data().tag3
          })
        })
      })
      .catch((err) => {
        console.log('Error getting documents', err)
      })
    this.all_picts = this.picts
    firebase.firestore().collection('tags').orderBy('count', 'asc').get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          console.log(doc.id, '=>', doc.data())
          this.tags.push({
            tagName: doc.id,
            count: doc.data().count
          })
        })
      })
      .catch((err) => {
        console.log('Error getting documents', err)
      })
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
