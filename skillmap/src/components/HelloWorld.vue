<template>
  <div id="skill-map">

    <button @click="onClickAddData()">add new data</button>
    <button @click="onClickOpenMemo()">memo</button><br>
    <div class='header'>
      <div class="categories">
        <div class="name-cell"></div>
        <div
          class="category"
          :class="{'frontend':cat.id === 1, 'backend':cat.id === 2, 'infra':cat.id === 3, 'research':cat.id === 4, 'other':cat.id === 5}"
          v-for="(cat, key) in skill_category_list"
          @click="addOpenFlg(cat.id)"
          :key="key"
        >
          {{cat.name}}
          <div class="skills">
            <div
              v-for="(skill, key) in getSkillsByCategoryId(cat.id)"
              :key="key"
            >
              <div
                class='skill'
                v-if="getIsOpen(cat.id)"
              >
                {{skill.name}}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="data-area">
      <div
        class="user-row"
        v-for="(user, key) in user_list"
        :key="key"
      >
        <div class="name-cell">
          {{user.name}}
        </div>
        <div
          class="category"
          :class="{'frontend':cat.id === 1, 'backend':cat.id === 2, 'infra':cat.id === 3, 'research':cat.id === 4, 'other':cat.id === 5}"
          v-for="(cat, key) in skill_category_list"
          @click="addOpenFlg(cat.id)"
          :key="key"
        >

          <div
            class="bar-area"
            :class="{ 'height-half':getIsOpen(cat.id), 'height-full':!getIsOpen(cat.id) }"
          >
            <div
              class="bar"
              :style="{ width: 100-getCategoryPercent(user.id, cat.id) + 'px' }"
            > </div>
          </div>
          <div class="skills" v-if="getIsOpen(cat.id)">
            <div
              v-for="(skill, key) in getSkillsByCategoryId(cat.id)"
              :key="key"
            >
              <div
                class='skill score-cell'
                v-if="getScoreByUidAndSid(user.id, skill.id)"
              >
                <div v-for="(star, key) in calcStar(getScoreByUidAndSid(user.id, skill.id))" :key="key">
                  {{ star }}
                </div>
              </div>
              <div v-else class='empty-skill'>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="isAddModalOpen" id="overlay">
      <div id="modal-content">
        <p>name: <input v-model="inputName" type=text><p>
        <div
          v-for="(cat, cat_key) in skill_category_list"
          :key="cat_key"
        >
          {{cat.name}}
          <button @click="onClickSkillPlus(cat.id)">+</button>
          <div
            v-for="(skill, skey) in getInputDataByCategoryId(cat.id)"
            :key="skey"
          >
            <div class="input-skill-row">
              <select v-model="skill.skill">
                <option
                  v-for="(skill, skey) in getSkillsByCategoryId(cat.id)"
                  :key="skey"
                >
                  {{skill.name}}
                </option>
                <option>
                  新規追加
                </option>
              </select>
              <div v-if="skill.skill === '新規追加'">
                項目名:<input type="text" v-model="skill.skillname">
              </div>
              <template v-if="inputData[skey]">
                <input type="range" min="1" max="5" v-model="skill.score">  {{skill.score}}
              </template>
            </div>
          </div>

        </div>
        <p>
          <button @click="onClickSubmit()">submit</button>
          <button @click="onClickClosemodal()">cancel</button>
        </p>
      </div>
    </div>

    <div v-if="isMemoModalOpen" id="overlay">
      <div id="modal-content">
        [todo]<br>
      ・データ編集<br>
      ・ソート<br>
      ・カラムはカラム合計でソートされるように<br>
        <button @click="onCliclCloseMemo()">cancel</button>

      </div>
    </div>

  </div>

</template>

<script>
import { SKILL_CATEGORY_LIST, SKILL_LIST, USER_LIST, USER_SKILLS } from '../data.js'

export default {
  name: 'HelloWorld',
  computed: {
    skill_category_list: function () {
      return SKILL_CATEGORY_LIST
    },
    skill_list: function () {
      return SKILL_LIST
    },
    user_list: function () {
      return USER_LIST
    },
    users_skills: function () {
      return USER_SKILLS
    },
    category_score_list: function () {
      let scoreList = []
      for (let user of this.user_list) {
        for (let category of this.skill_category_list) {
          let userSkills = this.getSkillsByUserId(user.id)
          let categorySkills = this.getSkillsByCategoryId(category.id)
          let total = 0
          for (let skill of categorySkills) {
            let s = userSkills.filter(x => x.sid === skill.id)[0]
            if (s) {
              total += parseInt(s.score)
            }
          }
          scoreList.push({
            'uid': user.id,
            'category_id': category.id,
            'score': total
          })
        }
      }
      return scoreList
    }
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      isSkillOpen: [],
      isAddModalOpen: false,
      inputName: undefined,
      isMemoModalOpen: false,
      inputData: [],
      inputSkills: [],
      inputScore: []
    }
  },
  methods: {
    getInputDataByCategoryId: function (categoryId) {
      return this.inputData.filter(x => x.category_id === categoryId)
    },
    getSkillsByCategoryId: function (categoryId) {
      return this.skill_list.filter(x => x.category_id === categoryId)
    },
    getSkillsByUserId: function (userId) {
      return this.users_skills.filter(x => x.uid === userId)
    },
    getSkillnameBySkillId: function (sid) {
      return this.skill_list.filter(x => x.id === sid)[0].name
    },
    getSkillIdBySkillName: function (skillName) {
      return this.skill_list.filter(x => x.name === skillName)[0].id
    },
    createKeyName: function (categoryId, inputKey) {
      return String(categoryId) + String(inputKey)
    },
    getScoreByUidAndSid: function (userId, skillId) {
      let data = this.users_skills.filter(x => x.uid === userId).filter(x => x.sid === skillId)[0]
      if (data) {
        return data.score
      } else {
        return data
      }
    },
    getIsOpen: function (categoryId) {
      return this.isSkillOpen.filter(x => x === categoryId).length >= 1
    },
    addOpenFlg: function (categoryId) {
      if (this.getIsOpen(categoryId)) {
        this.isSkillOpen = this.isSkillOpen.filter(x => x !== categoryId)
      } else {
        this.isSkillOpen.push(categoryId)
      }
    },
    calcStar: function (star) {
      let array = []
      for (let i = 0; i < star; i++) {
        array.push('★')
      }
      return array
    },
    getCategoryTotal: function (userId, categoryId) {
      return this.category_score_list.filter(x => x.uid === userId).filter(x => x.category_id === categoryId)[0].score
    },
    getCategoryPercent: function (userId, categoryId) {
      let array = []
      for (let cat of this.category_score_list.filter(x => x.category_id === categoryId)) {
        array.push(cat.score)
      }
      let maxScore = Math.max.apply(null, array)
      console.log(maxScore)
      return this.category_score_list.filter(x => x.uid === userId).filter(x => x.category_id === categoryId)[0].score / maxScore * 100
    },
    onClickAddData: function () {
      this.isAddModalOpen = true
    },
    onClickClosemodal: function () {
      this.isAddModalOpen = false
    },

    onClickOpenMemo: function () {
      this.isMemoModalOpen = true
    },
    onClickCloseMemo: function () {
      this.isMemoModalOpen = false
    },
    onClickSkillPlus: function (categoryId) {
      let inputSkillNames = []
      for (let data of this.inputData) {
        inputSkillNames.push(data.skill)
      }

      let notInputSkills = this.skill_list.filter(x => x.category_id === categoryId).filter(x => !inputSkillNames.includes(x.name))

      let nextSkill
      if (notInputSkills[0]) {
        nextSkill = this.getSkillnameBySkillId(notInputSkills[0].id)
      } else {
        nextSkill = '新規追加'
      }
      this.inputData.push({
        skill: nextSkill,
        score: 3,
        category_id: categoryId
      })
    },
    onClickSubmit: function () {
      let userIds = []
      for (let user of this.user_list) {
        userIds.push(user.id)
      }
      let nextUid = Math.max.apply(null, userIds) + 1
      this.user_list.push({
        id: nextUid,
        name: this.inputName
      })

      for (let data of this.inputData) {
        console.log(data.skill)
        if (data.skill === '新規追加') {
          let skillIds = []
          for (let skill of this.skill_list) {
            skillIds.push(skill.id)
          }
          let nextSid = Math.max.apply(null, userIds) + 1
          this.skill_list.push({
            id: nextSid,
            name: data.skillname,
            category_id: data.category_id
          })

          this.users_skills.push({
            uid: nextUid,
            sid: nextSid,
            score: data.score,
            starred: false
          })
        } else {
          this.users_skills.push({
            uid: nextUid,
            sid: this.getSkillIdBySkillName(data.skill),
            score: data.score,
            starred: false
          })
          this.inputName = undefined
          this.inputData = []
          this.isAddModalOpen = false
        }
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.frontend {
  color: #fef4f4;
  background-color: #f4b3c2;
}
.backend {
  color: #fef4f4;
  background-color: #84b9cb;
}
.infra {
  color: #fef4f4;
  background-color: #7ebea5;
}
.research {
  color: #fef4f4;
  background-color: #a59aca;
}
.other {
  color: #fef4f4;
  background-color: #f7b977;
}
.categories {
  border: 2px solid #000000;
  display: inline-flex;
  text-align: center;
}
.category {
  text-align: center;
  border-left: 2px solid #000000;
  min-width: 100px;
}
.bar-area{
  height:100%;
  width:100%;
  display: flex;
  flex-direction: row-reverse;
  margin-bottom: 3px;
}
.bar{
  background-color: white;
}
.height-full{
  height:100%;
}
.height-half{
  height:50%;
}
.skills {
  display: flex;
}
.empty-skill {
  display: flex;
  width:53px;
  font-size: 0.8em;
}
.skill {
  display: flex;
  margin: 1px;
  border: 1px solid #000000;
  width:50px;
  font-size: 0.8em;
}
.score-cell {
  font-size: 0.5em;
}
.user-row {
  margin: 2px;
  border: 2px solid #000000;
  /* background-color:bisque; */
  height:45px;
  display: inline-flex;
}
.name-cell {
  margin: 2px;
  display: flex;
  width: 100px;
}
#overlay{
  z-index:1;
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background-color:rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

#modal-content{
  text-align: left;
  max-height: 75%;
  overflow: scroll;
  z-index:2;
  width:75%;
  padding: 1em;
  background:#fff;
}
.input-skill-row{
  display:inline-flex;
}
#skill-map{
  text-align: left;
}
.header {
  position: fixed;
  /* left-margin:0px; */
  /* left: 2px; */
}
.data-area {
  position: fixed;
  top:60px;
  height:85%;
  overflow: scroll;
}
</style>
