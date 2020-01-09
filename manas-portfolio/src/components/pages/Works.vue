<template>
  <div id="works">
    <ContentField title='works'>
      <template slot="field-content">
        under construncting
      </template>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '../atoms/ContentField.vue'
export default {
  name: 'Works',
  components: {
    ContentField
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';

</style>
