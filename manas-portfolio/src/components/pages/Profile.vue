<template>
  <div id="profile">
    <ContentField title='profile'>
      <template slot="field-content">
        <h3>happy happy magician</h3>
        <h1>Mana（theta）</h1>
      </template>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '../atoms/ContentField.vue'
export default {
  name: 'Profile',
  components: {
    ContentField
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';

#profile{
  padding: $zero;
}

</style>
