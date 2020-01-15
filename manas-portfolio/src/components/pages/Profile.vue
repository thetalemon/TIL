<template>
  <div id="profile">
    <ContentField title='profile'>
      <template slot="field-content">
        <!-- <h3>happy happy magician</h3> -->
        <div id="center-area">
          <img id="prof-icon" src="../../assets/ico.jpg">
          <h1>Mana（theta）</h1>
        </div>
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
  #center-area{
    margin: 10px 0px;
    display: flex;
    #prof-icon {
        border-radius: 30%;
        width: 90px;
        height: 90px;
        margin-right: 30px;
    }
  }
}

</style>
