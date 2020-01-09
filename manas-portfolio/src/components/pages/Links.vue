<template>
  <div id="links">
    <ContentField title='links'>
      <template slot="field-content">
        tumblrとか
      </template>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '../atoms/ContentField.vue'
export default {
  name: 'Links',
  components: {
    ContentField
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';

</style>
