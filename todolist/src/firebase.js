import firebase from '@firebase/app'
import '@firebase/auth'
import '@firebase/firestore'
import store from './store'

const config = require('./config.js')

export default {
  init () {
    firebase.initializeApp(config.firebaseConfig)
    firebase.auth().setPersistence(firebase.auth.Auth.Persistence.SESSION)
  },
  login () {
    const provider = new firebase.auth.GoogleAuthProvider()
    firebase.auth().signInWithPopup(provider)
  },
  logout () {
    firebase.auth().signOut()
  },
  onAuth () {
    firebase.auth().onAuthStateChanged(user => {
      if (!user) user = {}
      store.commit('onAuthStateChanged', user)
      store.commit('onUserStatusChanged', Boolean(user.uid))
    })
  },
  getTodoItemList () {
    var comments = []
    firebase.firestore().collection('TODO_ITEM').orderBy('create_at', 'desc').get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          console.log(doc.id, '=>', doc.data())
          comments.push({
            content: doc.data().name,
            createdAt: doc.data().create_at.toDate().toLocaleString()
          })
        })
      })
      .catch((err) => {
        console.log('Error getting documents', err)
      })
    console.log(comments)
    return comments
  }
}
