<template>
  <div id="skills">
    <ContentField title='skills'>
      <template slot="field-content">
        <div>プログラミング</div>
        <div class="content">
          <ProgrammingSkillTip v-for="(value, key) in skills.programming"
            :key="key"
            :title="value.name"
            :star="value.star"
            :description="value.description"
          />
        </div>
        <div>資格</div>
        <div class="content">
          <QualificationSkillTip v-for="(value, key) in skills.Qualification"
            :key="key"
            :title="value.name"
            :date="value.date"
          />
        </div>
        <div>その他</div>
        <div class="content">
          <ProgrammingSkillTip v-for="(value, key) in skills.other"
            :key="key"
            :title="value.name"
            :description="value.description"
          />
        </div>
      </template>
    </ContentField>
  </div>
</template>

<script>
import ContentField from '../atoms/ContentField.vue'
import ProgrammingSkillTip from '../atoms/ProgrammingSkillTip.vue'
import QualificationSkillTip from '../atoms/QualificationSkillTip.vue'
import { SKILLS } from '../../skills.js'
export default {
  name: 'Skills',
  components: {
    ContentField,
    ProgrammingSkillTip,
    QualificationSkillTip
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
