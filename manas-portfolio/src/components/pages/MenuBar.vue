<template>
  <div class="menubar">
    <MenuBarItem msg='profile' />
    <MenuBarItem msg='skills' />
    <MenuBarItem msg='works' />
    <MenuBarItem msg='links' />
  </div>
</template>

<script>
import MenuBarItem from '../atoms/MenuBarItem.vue'
export default {
  name: 'MenuBar',
  components: {
    MenuBarItem
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.menubar {
  justify-content: center;
  display: flex;
}
</style>
