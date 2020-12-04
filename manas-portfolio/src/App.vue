<template>
  <div id="app">
    <EyeCatch/>
    <MenuBar/>
    <Profile name="profile"/>
    <Skills/>
    <Works/>
    <Links/>
  </div>
</template>

<script>
import EyeCatch from './components/pages/EyeCatch.vue'
import Links from './components/pages/Links.vue'
import MenuBar from './components/pages/MenuBar.vue'
import Profile from './components/pages/Profile.vue'
import Skills from './components/pages/Skills.vue'
import Works from './components/pages/Works.vue'

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

<style lang="scss" scoped>
@import './unified.scss';
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: $light-font-color;
  background-color: $main-background-color;
  padding: $micro $zero;
}
</style>
