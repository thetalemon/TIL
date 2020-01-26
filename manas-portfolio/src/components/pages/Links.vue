<template>
  <div id="links">
    <ContentField title='links'>
      <template slot="field-content">
        <div class="content">
          <div v-for="(value, key) in links"
            :key="key"
          >
          <a :href="value.url">
            {{value.name}}
          </a>
          </div>
        </div>
      </template>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '../atoms/ContentField.vue'
import { LINKS } from '../../skills.js'
export default {
  name: 'Links',
  components: {
    ContentField
  },
  computed: {
    links: function () {
      return LINKS
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';

</style>
