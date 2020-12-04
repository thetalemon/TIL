<template>
  <div class="menubar-item">
    <a :href="anchor">{{text}}</a>
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  props: {
    text: String
  },
  computed: {
    anchor: function () {
      return '#' + this.text
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';
.menubar-item {
  margin: $zero $little;
  padding: $micro $little;
  background-color: $dark-background-color;
  color: $light-font-color;

  a {
    text-decoration: none;
  }
  a:link { color: $light-font-color; }
  a:visited { color: $light-font-color; }
  a:hover { color: #ffffff; }
  a:active { color: #ffffff; }
}
</style>
