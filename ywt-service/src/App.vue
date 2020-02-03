<template>
  <div id="app">
    <textarea v-model="message" placeholder="add multiple lines"></textarea><br>
    <div style="white-space:pre-wrap; word-wrap:break-word;">{{message}}</div><br>
    <!-- <div v-for="(row, key) in messages" :key="key">
      {{row}}
    </div> -->
    <div @click="convert()">convert!</div>
    <div style="white-space:pre-wrap; word-wrap:break-word;">{{converted}}</div><br>
    <!-- {{converted}}<br> -->
    <br>
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

export default {
  name: 'app',
  components: {
  },
  data: function () {
    return {
      message: '',
      converted: '',
      output_text: '',
      item:{}
    }
  },
  computed: {
    // messages: function () {
    //   var textArray = this.message.split(/\r\n|\r|\n/);
    //   textArray.match(/[^-.*]/g)
    //   // for(text of textArray){
    //   //
    //   // }
    //   return textArray.match(/[^-.*]/g)
    // }
  },
  methods: {
    convert: function () {
      var textArray = this.message.split(/\r\n|\r|\n/);
      let matchingArray = []
      for(let text of textArray){
        if(text.match(/^[-].*/g)){
          matchingArray.push(text.match(/^[-].*/g))
        }
      }
      this.converted = matchingArray
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
