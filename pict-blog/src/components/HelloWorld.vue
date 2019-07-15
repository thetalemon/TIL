<template>
  <div class="hello">
    <h1>Hello {{ name }}!!</h1>
    <h1>{{ msg }}</h1>

    <button @click="signOut">Sign out</button>
    <table align="center">
      <tr>発言一覧</tr>
      <tr v-for="(comment, index) in comments" :key="index">
        <td><img class="top" :src="comment.avatar" v-on:click="show"></td>
        <modal name="img-modal" :adaptive="true"  width="80%" height="80%">
          <p><img :src="comment.avatar" v-on:click="show"></p>
          <p>{{comment.content}}</p>
          <p>{{comment.createdAt}}</p>
          <p><button v-on:click="hide">hide</button></p>
        </modal>
      </tr>
    </table>
      <!-- <button v-on:click="show">show!</button> -->
  </div>
</template>

<script>
import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/firestore'
// import VModal from 'vue-js-modal'
// import VModal from 'vue-js-modal'
// Vue.use(VModal)

export default {
  component: ('modal', {
    template: '#modal-template'
  }),
  name: 'HelloWorld',
  // el: '.l-wrapper',
  data: () => ({
    msg: 'Welcome to Your Vue.js App',
    name: firebase.auth().currentUser.email,
    comments: []
  }),
  methods: {
    signOut: function () {
      firebase.auth().signOut().then(() => {
        this.$router.push('/signin')
      })
    },
    show: function () {
      this.$modal.show('img-modal')
    },
    hide: function () {
      this.$modal.hide('img-modal')
    }
  },
  created: function () {
    firebase.firestore().collection('comments').get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          console.log(doc.id, '=>', doc.data())
          this.comments.push({
            avatar: doc.data().avatar,
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
/* ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
} */
/* a {
  color: #42b983;
} */
.hello{
 text-align: center;
}
table{
  border: 2px #2b2b2b solid;
}
td{
 text-align: center;
}
img {
  align:center;
  padding: 30px;
  margin: 20px;
}
div {
  text-align:center;
}
modal{
  text-align:center;
}
img.top {
  width: 250px;
  height: 250px;
  object-fit: cover; /* この一行を追加するだけ！ */
}

p{
  text-align: center;
}

</style>
