<template>
  <div class="content-field">
    <div class="title">
      <div class="title-text">{{title}} </div>
      <Stars :star="star" />
    </div>
    <div class="content">
      {{description}}
    </div>
  </div>
</template>

<script>
import Stars from '../atoms/stars.vue'
export default {
  name: 'MenuBar',
  components: {
    Stars
  },
  props: {
    title: String,
    star: Number,
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
    display: flex;
    text-align: left;
    padding: $micro $zero;
    padding-left: $little;
    color: $light-font-color;
    background-color: $dark-background-color;
    font-size: $font-big;
    .title-text {
        width:120px;
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
