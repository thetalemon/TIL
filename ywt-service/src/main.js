import Vue from 'vue'
import App from './App.vue'
import store from "./store";

Vue.config.productionTip = false

import Firebase from "./firebase";
Firebase.init();

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
