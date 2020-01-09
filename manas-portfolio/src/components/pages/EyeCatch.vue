<template>
  <div id="eye-catch">
    <img src="../../assets/IMG_0235.jpg">
    <div>M's portfolio</div>
  </div>
</template>

<script>
export default {
  name: 'EyeCatch',
  props: {
    msg: String
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';
#eye-catch {
  background-color: $dark-background-color;
  padding: $wide $zero;
  margin: $little $little;
  img{
    width: 200px;
  }
}
</style>
