<template>
  <div class="skill-tip">
    <div class="title">
      <div class="title-text">{{title}} </div>
    </div>
    <div class="content">
      {{date}}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuBar',
  props: {
    title: String,
    date: String
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';
.skill-tip {
  width: 200px;
  justify-content: start;
  .title{
    display: flex;
    text-align: left;
    padding: $micro $zero;
    padding-left: $little;
    color: $light-font-color;
    background-color: $dark-background-color;
    font-size: $font-big;
    .title-text {
        width:200px;
    }
  }
  .content{
    text-align: left;
    padding: $micro $zero;
    padding-left: $little;
    color: $dark-font-color;
    background-color: #ffffff;
  }
  margin: $little $little;
}
</style>
