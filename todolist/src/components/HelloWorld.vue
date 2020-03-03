<template>
  <div class="hello">
    aaaa
    <Navigation />
    aaa
    {{todo_item_list}}
  </div>
</template>

<script>
import Firebase from './../firebase'
import Navigation from '@/components/Nav.vue'
export default {
  name: 'HelloWorld',
  components: {
    Navigation
  },
  data () {
    return {
      todo_item_list: []
    }
  },
  created: function () {
    this.todo_item_list = Firebase.getTodoItemList()
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
