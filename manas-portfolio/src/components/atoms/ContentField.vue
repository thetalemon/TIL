<template>
  <div class="content-field">
    <div class="title">
      {{title}}
    </div>
    <div class="content">
      <slot name="field-content" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  props: {
    title: String
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';
.content-field {
  justify-content: start;
  .title{
    text-align: left;
    padding: $micro $zero;
    padding-left: $little;
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
