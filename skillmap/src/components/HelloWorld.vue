<template>
  <div id="skill-map">
    [memo]<br>
    ・データ編集<br>
    ・ソート<br>
    ・カラムはカラム合計でソートされるように<br>
    ・合計を視覚的に<br>

    <button @click="onClickAddData()">add new data</button>
    <div class="categories">
      <div class="name-cell"></div>
      <div
        class="category"
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
    <div>
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
          v-for="(cat, key) in skill_category_list"
          @click="addOpenFlg(cat.id)"
          :key="key"
        >
            {{calcCategoryTotal(user.id, cat.id)}}
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
    <div v-if="isModalOpen" id="overlay">
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
    }
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      isSkillOpen: [1, 2],
      isModalOpen: false,
      inputName: undefined,
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
    calcCategoryTotal: function (userId, categoryId) {
      let userSkills = this.getSkillsByUserId(userId)
      let categorySkills = this.getSkillsByCategoryId(categoryId)
      let total = 0
      for (let skill of categorySkills) {
        let s = userSkills.filter(x => x.sid === skill.id)[0]
        if (s) {
          total += parseInt(s.score)
        }
      }
      return total
    },
    onClickAddData: function () {
      this.isModalOpen = true
    },
    onClickClosemodal: function () {
      this.isModalOpen = false
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
          this.isModalOpen = false
        }
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.categories {
  border: 2px solid #000000;
  display: inline-flex;
  text-align: center;
}
.category {
  text-align: center;
  margin: 2px;
  border-left: 2px solid #000000;
  min-width: 200px;
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
  background-color:bisque;
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
</style>
