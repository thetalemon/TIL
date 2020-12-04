<template>
  <div class="stars">
    <div v-for="(a, key) in calcStar(star)" :key="key">
      {{ a }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Stars',
  props: {
    star: Number
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
