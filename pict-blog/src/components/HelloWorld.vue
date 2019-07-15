<template>
  <div class="hello">
    <h1>Hello {{ name }}!!</h1>

    <!-- 投稿フォーム -->
    <button v-on:click="show_submit">投稿する</button>
    <modal name="submit_modal" :adaptive="true"  width="80%" height="80%">
      <p><canvas ref="canvas" class="resize-img__preview__canvas"/></p>
      <p><input type="file" @change="onFileChange"></p>
    </modal>

    <!-- 投稿一覧 -->
    <ul  class="box-list">
      <li v-for="(comment,key, index) in comments" :key="index">
        <div><img class="top" :src="comment.content" v-on:click="show_img(key)"></div>
        <modal name="img_modal" :adaptive="true"  width="80%" height="80%">
          <p><img :src="modal_img"></p>
          <p>{{modal_createdAt}}</p>
          <p><button v-on:click="hide">hide</button></p>
        </modal>
      </li>
    </ul>

  </div>
</template>

<script>
import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/firestore'

export default {
  name: 'HelloWorld',
  data: () => ({
    name: firebase.auth().currentUser.email,
    comments: [],
    modal_img: '',
    modal_createdAt: '',
    uploadImage: ''
  }),
  methods: {
    onFileChange (e) {
      e.preventDefault()

      var file = e.target.files[0]
      const reader = new FileReader()
      reader.onload = (e) => {
        this.generateImgUrl(e.target.result)
      }
      reader.readAsDataURL(file)
    },
    generateImgUrl (file) {
      const image = new Image()
      image.crossOrigin = 'Anonymous'
      image.onload = (e) => {
        // データを指定した後の処理
        // リサイズ・現在時刻取得
        const resizedBase64 = this.makeResizeImg(image)
        let timestamp = firebase.firestore.FieldValue.serverTimestamp()

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
      return canvas.toDataURL('image/jpeg')
    },
    signOut: function () {
      firebase.auth().signOut().then(() => {
        this.$router.push('/signin')
      })
    },
    show_submit: function (key) {
      this.$modal.show('submit_modal')
    },
    hide_submit: function () {
      this.$modal.hide('submit_modal')
    },
    show_img: function (key) {
      this.$modal.show('img_modal')
      // モーダル内の画像を対象画像に差し替える
      this.modal_img = this.comments[key].content
      this.modal_createdAt = this.comments[key].createdAt
    },
    hide: function () {
      this.$modal.hide('img_modal')
    }
  },
  created: function () {
    firebase.firestore().collection('picts').orderBy('createdAt', 'desc').get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          console.log(doc.id, '=>', doc.data())
          this.comments.push({
            content: doc.data().content,
            createdAt: doc.data().createdAt.toDate().toLocaleString()
          })
        })
      })
      .catch((err) => {
        console.log('Error getting documents', err)
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
  /* align:center; */
  /* padding: 0px; */
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
  /* justify-content: space-between; */
  flex-flow: row wrap;

}
.box-list li{
  flex: 0 0 10%;
  /* border: 1px solid #ccc; */
  margin-bottom: 0px;
}
/* img{
  width: 100%;
} */

</style>
