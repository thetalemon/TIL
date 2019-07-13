<template>
  <div class="hello">
    <h1>Hello {{ name }}!!</h1>
    <h1>{{ msg }}</h1>
    <!-- <h2>Essential Links</h2>
    <ul>
      <li><a href="https://vuejs.org" target="_blank">Core Docs</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">Forum</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank">Community Chat</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">Twitter</a></li>
      <br>
      <li><a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a></li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">vue-router</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">vuex</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a></li>
    </ul> -->
    <button @click="signOut">Sign out</button>
      <table>
        <tr>発言一覧</tr>
        <!-- <tr>{{comments}}<tr> -->
        <tr v-for="(comment, index) in comments" :key="index">
        <td><img :src="comment.avatar"></td>
          <td>{{comment.content}}</td>
            <td>{{comment.createdAt}}</td>
        <td>{{comment.id}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/firestore'

export default {
  name: 'HelloWorld',
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
  // firestore () {
  //   return {
  //     // firestoreのcommentsコレクションを参照
  //     comments: firebase.firestore().collection('comments').orderBy('createdAt')
  //   }
  // }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
