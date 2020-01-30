<template>
  <div id="app">
    <textarea v-model="message" placeholder="add multiple lines"></textarea><br>
    <div style="white-space:pre-wrap; word-wrap:break-word;">{{message}}</div><br>
    <div v-for="(row, key) in messages" :key="key">
      {{row}}
    </div>
    <div @click="convert()">convert!</div>
    {{converted}}<br>
    <br>
    ↑に過去のYWTをおいてそれをパースできるようにする<br>
    なんか入力欄<br>
    項目名<input></input><br>
    よていは<br>
    やった<br>
    わかった<br>
    つぎは<br>
    outputボタン<br>
    ここにアウトプットが出力されるテキストボックスをおく<br>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    // HelloWorld
  },
  data: function () {
    return {
      message: '',
      converted: ''
    }
  },
  computed: {
    messages: function () {
      var textArray = this.message.split(/\r\n|\r|\n/);
      return textArray
    }
  },
  methods: {
    convert: function () {
      this.converted = this.message
    }
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
