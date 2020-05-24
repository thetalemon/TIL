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
  getBookList () {
    console.log('getBookList')

    var comments = []
    firebase.firestore().collection('BOOK_LIST').where('uid', '==', store.state.user.uid).orderBy('create_at', 'desc').get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          // console.log(doc.id, '=>', doc.data())
          comments.push({
            name: doc.data().name,
            all: doc.data().all,
            uid: doc.data().uid,
            createdAt: doc.data().create_at.toDate().toLocaleString()
          })
        })
      })
      .catch((err) => {
        console.log('Error getting documents', err)
      })
    return comments
  },
  insertTodoItemList (bookName, bookAll) {
    firebase.firestore().collection('BOOK_LIST').add({
      name: bookName,
      all: parseInt(bookAll),
      uid: store.state.user.uid,
      create_at: firebase.firestore.FieldValue.serverTimestamp()
    }).then(ref => {
      console.log('Added document with ID: ', ref.id)
      return ref
    })
  },
  getBookProgress () {
    console.log('getBookProgress')
    var comments = []
    firebase.firestore().collection('BOOK_PROGRESS_LIST').where('uid', '==', store.state.user.uid).orderBy('create_at', 'desc').get()
      .then((snapshot) => {
        snapshot.forEach((doc) => {
          // console.log(doc.id, '=>', doc.data())
          comments.push({
            name: doc.data().name,
            current: doc.data().current,
            createdAt: doc.data().create_at.toDate().toLocaleString()
          })
        })
      })
      .catch((err) => {
        console.log('Error getting documents', err)
      })
    return comments
  },
  insertBookProgress (bookName, currentProgress) {
    firebase.firestore().collection('BOOK_PROGRESS_LIST').add({
      name: bookName,
      current: parseInt(currentProgress),
      uid: store.state.user.uid,
      create_at: firebase.firestore.FieldValue.serverTimestamp()
    }).then(ref => {
      console.log('Added document with ID: ', ref.id)
      return ref
    })
  }
}
