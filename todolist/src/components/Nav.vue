<!-- 引用元 : https://qiita.com/ErgoFriend/items/bd1bb445e185bf45e272 -->
<template>
    <div id="nav">
      <nav class="navbar is-transparent" v-bind:class="{'is-fixed-bottom':menuPosition}">
        <div class="navbar-brand">
          <!-- <router-link class="navbar-item" to="/">
            <img src="https://bulma.io/images/bulma-logo.png" alt="Bulma: a modern CSS framework based on Flexbox" width="112" height="28">
          </router-link> -->
          <div class="navbar-burger burger " v-bind:class="{ 'is-active': menuActive }" v-on:click="menuToggle()" data-target="navbarExampleTransparentExample">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
        <div id="navbarExampleTransparentExample" class="navbar-menu" v-bind:class="{ 'is-active': menuActive }">
          <div class="navbar-start">
            <!-- <router-link class="navbar-item" to="/">Home</router-link>
            <router-link class="navbar-item" to="/about">About</router-link> -->
          </div>
          <div class="navbar-end">
            <Authentication />
          </div>
        </div>
      </nav>
    </div>
</template>
<script>
import Authentication from '@/components/Auth.vue'
export default {
  name: 'navigation',
  components: {
    Authentication
  },
  created () {
    if (window.innerWidth < 920) {
      this.menuPosition = !this.menuPosition
    }
  },
  data () {
    return {
      menuActive: false,
      menuPosition: false
    }
  },
  methods: {
    menuToggle () {
      this.menuActive = !this.menuActive
    }
  }
}
</script>

<style scoped>
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #555;
}
#nav a.router-link-exact-active {
  color: #3273dc;
}
</style>
