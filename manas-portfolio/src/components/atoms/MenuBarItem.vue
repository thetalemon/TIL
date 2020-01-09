<template>
  <div class="menubar-item">
    {{msg}}
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  props: {
    msg: String
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
}
</style>
