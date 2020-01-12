<template>
  <div class="stars">
    <div v-for="a in calcStar(star)" :key="a">
      {{ a }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Stars',
  props: {
    title: String,
    star: Number,
    description: String
  },
  methods: {
    calcStar: function (star) {
      let array = []
      for(let i = 0; i < star; i++){
        array.push('★')
      }
      return array
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';
.stars {
  display: flex;
}
</style>
