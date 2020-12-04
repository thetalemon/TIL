<template>
  <div id="app">
    <Navigation />

    <textarea v-model="message" placeholder="add multiple lines"></textarea><br>
    <div style="white-space:pre-wrap; word-wrap:break-word;">{{message}}</div><br>
    <div @click="convert()">convert!</div>
    <div style="white-space:pre-wrap; word-wrap:break-word;">{{converted}}</div><br>
    <div style="white-space:pre-wrap; word-wrap:break-word;">{{converted_bottom}}</div><br>
    <br>
    {{user.displayName}}
    項目名:<input v-model="item.name" placeholder="edit me"><br>
    よていは:<input v-model="item.plan" placeholder="edit me"><br>
    やった:<input v-model="item.y" placeholder="edit me"><br>
    わかった:<input v-model="item.w" placeholder="edit me"><br>
    つぎは:<input v-model="item.t" placeholder="edit me"><br>
    <br>
    <div @click="output()">output!</div>
    {{output_text}}<br>
    <br>
    <textarea class="output-area" v-model="output_text" placeholder="add multiple lines"></textarea><br>

  </div>
</template>

<script>
import Navigation from "@/components/Nav.vue";
export default {
  name: 'app',
  components: {
    Navigation
  },
  data: function () {
    return {
      message: '',
      converted: '',
      converted_bottom: '',
      output_text: '',
      item:[]
    }
  },
  computed: {

      user() {
        return this.$store.getters.user;
      },
  },
  methods: {
    convert: function () {
      var textArray = this.message.split(/\r\n|\r|\n/);

      let all_content_set = []
      let current_content_set = undefined

      for(let text of textArray){
        if(text.match(/^[-].*/g)){
          // 次のコンテンツになったら前のコンテンツは配列にいれて現在のコンテンツを保つ変数を初期化
          if(current_content_set){
            all_content_set.push(current_content_set)
          }
          current_content_set = {
            name: undefined,
            content: []
          }
          let name = text.match(/^[-].*/g)[0].replace(/^[-][ ]/g, '')
          current_content_set.name = name
        }
        if(text.match(/^[ ]{4}[-].*/g)){
          let content = text.match(/^[ ]{4}[-].*/g)[0].replace(/^[ ]{4}[-][ ]/g, '')
          current_content_set.content.push(content)
        }
      }
      all_content_set.push(current_content_set)
      this.converted_bottom = all_content_set
    },
    output: function () {
      this.output_text = this.item.name + '\n' + this.item.plan + '\n' + this.item.y + '\n' + this.item.w + '\n' + this.item.t
    }
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
.output-area {
  width:500px;
  height:300px;
}
</style>
