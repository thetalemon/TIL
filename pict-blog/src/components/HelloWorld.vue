<template>
  <div class="hello">
    <h1>Hello {{ name }}!!</h1>
    <h1>{{ msg }}</h1>

    <button @click="signOut">Sign out</button>
      <table>
        <tr>発言一覧</tr>
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
