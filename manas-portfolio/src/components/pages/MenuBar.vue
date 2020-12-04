<template>
  <div class="menubar">
    <MenuBarItem text='profile'/>
    <MenuBarItem text='skills'/>
    <MenuBarItem text='works'/>
    <MenuBarItem text='links'/>
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

<style scoped>
.menubar {
  justify-content: center;
  display: flex;
}
</style>
