<template>
  <div class="content-field">
    <div class="title">
      {{title}}
      {{star}}
      {{description}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  props: {
    title: String,
    star: String,
    description: String
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';
.content-field {
  width: 200px;
  justify-content: start;
  .title{
    text-align: left;
    padding: $micro $zero;
    padding-left: $little;
    color: $light-font-color;
    background-color: $dark-background-color;
    font-size: $font-big;
  }
  .content{
    text-align: left;
    padding: $micro $zero;
    padding-left: $little;
    color: $dark-font-color;
    background-color: $light-background-color;
  }
  margin: $little $little;
  // padding: $micro $little;
}
</style>
