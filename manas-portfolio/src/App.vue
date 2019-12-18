<template>
  <div id="app">
    <EyeCatch msg="Welcome to Your Vue.js App"/>
    <MenuBar msg="Welcome to Your Vue.js App"/>
    <Profile msg="Welcome to Your Vue.js App"/>
    <Skills msg="Welcome to Your Vue.js App"/>
    <Works msg="Welcome to Your Vue.js App"/>
    <Links msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import EyeCatch from './components/EyeCatch.vue'
import Links from './components/Links.vue'
import MenuBar from './components/MenuBar.vue'
import Profile from './components/Profile.vue'
import Skills from './components/Skills.vue'
import Works from './components/Works.vue'

export default {
  name: 'app',
  components: {
    EyeCatch,
    Links,
    MenuBar,
    Profile,
    Skills,
    Works
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
