<template>
  <div id="eye-catch">
    <div id="eye-catch-image">M's portfolio</div>
    <img src="../../assets/IMG_8003.jpg">
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
  position: relative;
  background-color: $dark-background-color;
  margin: $little $little;
  padding: $micro;
  height: 300px;
  #eye-catch-image {
    position: absolute;
    color: $dark-background-color;
    top: 150px;
    left: 50px;
    font-size: 2.0em;
  }
  img{
    width: 100%;
    height: 300px;
    object-position: 100% 50%;
    object-fit: cover;
  }
}
</style>
