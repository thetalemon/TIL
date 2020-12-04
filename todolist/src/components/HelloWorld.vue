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
import { mapState } from 'vuex'
export default {
  name: 'HelloWorld',
  components: {
    Navigation
  },
  computed: mapState(['user']),
  watch: {
    user: function () {
      if (this.user.displayName) {
        Firebase.insertTodoItemList()
      }
    }
  },
  data () {
    return {
      todo_item_list: []
    }
  },
  created: function () {
    // TODO これでちゃんとデータはとれるが、いれたてほやほやのデータでエラーになる
    this.todo_item_list = Firebase.getTodoItemList()
  }
}
</script>

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
