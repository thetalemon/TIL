<template>
  <div id="skills">
    <ContentField title='skills'>
      <template slot="field-content">
        <div class="content">
          <SkillTip v-for="(value, key) in skills"
            :key="key"
            :title="value.name"
            :star="value.star"
            :description="value.description"
          />
        </div>
      </template>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '../atoms/ContentField.vue'
import SkillTip from '../atoms/SkillTip.vue'
import { SKILLS } from '../../skills.js'
export default {
  name: 'Skills',
  components: {
    ContentField,
    SkillTip
  },
  computed: {
    skills: function () {
      return SKILLS
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../unified.scss';
.content {
  background-color: red;
  display: flex;
  flex-wrap : wrap;
}

</style>
