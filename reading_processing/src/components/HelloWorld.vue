<template>
  <div id="main">
    <Authentication />
    <div v-if="!isLoggedin" id="content">
            ログインしてください
    </div>

    <div v-else id="content">
      <div class="button add-new-book-button" @click="onClickPostNewItem()">新しい本を登録する</div>
      <div class="row">
        <div class="book-name">書籍名</div>
        <div class="progress">進捗率</div>
        <div class="last-update">最終更新</div>
      </div>
      <div v-if="isLoaded">
        <div class="row" v-for="(item,key, index) in adjusted_book_list" :key="index">
          <div class="book-name" @click="onClickBookDetail(item)">{{item.name}}</div>
          <div class="progress" @click="onClickUpdateBookProgress(item)">
            <div class="bar-area">
              <div
                class="bar"
                :style="{ width: item.percent + '%' }"
              > </div>
            </div>
          </div>
          <div class="last-update" @click="onClickBookDetail(item)">{{item.createdAt}}</div>
        </div>
      </div>
    </div>

    <!-- <div v-else>
      loading...
    </div> -->

    <div v-if="isAnyModalOpen " id="window">
      <div @click="onClickCloseModal()" v-if="isAnyModalOpen " id="overlay">
      </div>

      <div v-if="isAnyModalOpen" id="modal-area">
        <div class="mordal-close-button-area">
          <div><div class="book-name-text" v-if="isUpdateProgressModalOpen || isBookDetailModalOpen">{{currentBookData.name}}</div></div>
          <div @click="onClickCloseModal()" class="mordal-close-button">
            ×
          </div>
        </div>

        <div v-if="isPostNewItemModalOpen" id="modal-content">
          <div class="flex">
              <div class="input-text-area">書籍名</div>
              <input type="text" placeholder="書籍名" v-model="insertNewBook"></div>
          <div class="flex">
            <div class="input-text-area">総ページ数</div>
            <input type="number" placeholder="総ページ数" v-model="insertNewBookAll">
          </div>
          <div id="mordal-buttons-area" class="flex">
            <div class="button submit-button" @click="post_new_item()">submit</div>
            <div class="button" @click="onClickClosePostNewItemModal()">cancel</div>
          </div>
        </div>

        <div v-if="isUpdateProgressModalOpen" id="modal-content">
          <div class="flex">
            <div class="input-text-area">現在<br>ページ
            </div>
            <input type="number" placeholder="現在ページ" v-model="insertNewProgress">
            <div class="all-pages-text"> <p>/ {{currentBookData.all}}</p></div>
          </div>
          <div id="mordal-buttons-area" class="flex">
            <div class="button submit-button" @click="post_progress()">submit</div>
            <div class="button" @click="onClickCloseModal()">cancel</div>
          </div>
        </div>

        <div v-if="isBookDetailModalOpen" id="modal-content">
          <div class="progress-history big-font">進捗履歴</div>
          <div class="row" v-for="(item,key, index) in getCurrentBookProgressHistory(currentBookData.name)" :key="index">
            <div class="bar-area">
              <div
                class="bar"
                :style="{ width: getCategoryPercent(item.current, currentBookData.all) + '%' }"
              > </div>
            </div>
            <div>{{getCategoryPercent(item.current, currentBookData.all)}}</div>
            <div class="create-at">{{item.createdAt}}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Authentication from '@/components/Auth.vue'
import Firebase from './../firebase'
import { mapState } from 'vuex'
export default {
  name: 'HelloWorld',
  components: {
    Authentication
  },
  computed:
  {
    ...mapState(['user']),
    isAnyModalOpen () {
      return this.isPostNewItemModalOpen || this.isUpdateProgressModalOpen || this.isBookDetailModalOpen
    },
    isLoggedin () {
      return Boolean(this.user.displayName)
    },
    isLoaded () {
      return this.book_item_list.length && this.BookProgressHistory.length
    },
    adjusted_book_list () {
      if (!this.BookProgressHistory.length) return []
      let list = []
      for (let item of this.book_item_list) {
        let hist = this.getCurrentBookProgressHistory(item.name)[0]
        if (hist) {
          list.push({
            name: item.name,
            all: item.all,
            current: hist.current,
            createdAt: hist.createdAt,
            percent: (hist.current / item.all * 100)
          })
        } else {
          list.push({
            name: item.name,
            all: item.all,
            current: 0,
            createdAt: item.createdAt,
            percent: 0
          })
        }
      }
      console.log(list)

      return list
    }
  },
  watch: {
    user: function () {
      if (this.user.displayName) {
        console.log(this.user.uid)
        this.book_item_list = Firebase.getBookList()
        this.BookProgressHistory = Firebase.getBookProgress()
      }
    }
  },
  data () {
    return {
      book_item_list: [],
      isPostNewItemModalOpen: false,
      isUpdateProgressModalOpen: false,
      isBookDetailModalOpen: false,
      insertNewBook: undefined,
      insertNewBookAll: 0,
      insertNewProgress: 0,
      currentBookData: undefined,
      BookProgressHistory: []
    }
  },
  created: function () {
  },
  methods: {
    getNow: function (name) {
      var now = new Date()

      var Year = now.getFullYear()
      var Month = now.getMonth() + 1
      var Day = now.getDate()
      var Hour = now.getHours()
      var Min = now.getMinutes()
      var Sec = now.getSeconds()

      return (Year + '/' + Month + '/' + Day + '' + Hour + ':' + Min + ':' + Sec)
    },
    getCurrentBookProgressHistory: function (name) {
      if (this.BookProgressHistory.lnegth) return []
      return this.BookProgressHistory.filter(x => x.name === name)
    },
    getCurrentBookProgress: function (name) {
      let hist = this.getCurrentBookProgressHistory(name)
      if (!hist.length) return 0
      return this.getCurrentBookProgressHistory(name)[0].current
    },
    getCurrentBookLastUpdate: function (name) {
      let hist = this.getCurrentBookProgressHistory(name)
      if (!hist.length) return 0
      return this.getCurrentBookProgressHistory(name)[0].create_at
    },
    onClickPostNewItem: function () {
      this.isPostNewItemModalOpen = true
    },
    onClickClosePostNewItemModal: function () {
      this.isPostNewItemModalOpen = false
    },
    onClickUpdateBookProgress: function (item) {
      this.isUpdateProgressModalOpen = true
      this.currentBookData = item
      this.insertNewProgress = this.getCurrentBookProgress(item.name)
    },
    onClickBookDetail: function (item) {
      this.isBookDetailModalOpen = true
      this.currentBookData = item
    },
    onClickCloseModal: function () {
      this.isPostNewItemModalOpen = false
      this.isUpdateProgressModalOpen = false
      this.isBookDetailModalOpen = false
      this.currentBookData = undefined
    },
    getCategoryPercent: function (current, all) {
      return (current / all * 100).toFixed()
    },
    post_new_item: function () {
      this.book_item_list.unshift({
        name: this.insertNewBook,
        all: this.insertNewBookAll,
        createdAt: this.getNow()
      })
      Firebase.insertTodoItemList(this.insertNewBook, this.insertNewBookAll)
      this.insertNewBook = undefined
      this.insertNewBookAll = 0
      this.onClickCloseModal()
    },
    post_progress: function () {
      this.BookProgressHistory.unshift({
        name: this.currentBookData.name,
        current: this.insertNewProgress,
        createdAt: this.getNow()
      })
      Firebase.insertBookProgress(this.currentBookData.name, this.insertNewProgress)
      this.insertNewProgress = 0
      this.onClickCloseModal()
    }
    // update_book_progress: function () {
    //     Firebase.insertTodoItemList()
    // }
  }
}
</script>

<style scoped>
.book-name-text {
  font-size:1.5em;
  margin-bottom: 20px;
}
.all-pages-text{
  width: 50px;
}
input {
  border: 1px solid;
}
.big-font{
  font-size: 1.2em;
}
.progress-history{
  margin-bottom: 15px;
}
.bar{
  height:100%;
  background-color: #ffaabb;
}
.bar-area{
  height: 30px;
  width: 100%;
}
#content{
  /* position: fixed; */
  justify-content: center;
  /* top:5px;
  left:5px; */
  /* height:100%; */
  padding:5px;

  /* margin-left: auto;
  margin-right: auto; */
  /* background-color:red; */
}

#main{
  /* position: fixed; */
  justify-content: center;
  /* top:5px;
  left:5px; */
  height:100%;
  padding:5px;

  /* margin-left: auto;
  margin-right: auto; */
  /* background-color:red; */
}
.submit-button {
  margin-right: 5px;
}
.button {
  padding: 2px 10px 2px 10px;
  border-radius: 5px;
  background-color: #2222bb;
  color: #ccccff;
}
.mordal-close-button-area {
  font-size: 1.3em;
  display: flex;
  justify-content: space-between;
  /* justify-content: flex-end; */
  padding-left: 10px;
}
.mordal-close-button {
  font-size: 1.3em;
  padding-right: 8px;
}
.input-text-area{
  width:100px;
}
.add-new-book-button{
  margin-bottom: 10px;;
}
#mordal-buttons-area{
  margin-top: 20px;
  justify-content: flex-end;
}
.flex {
  display: flex;
}
.row{
  min-height: 30px;
  display: flex;
  width: 100%;
  margin-bottom: 3px;
}
.book-name {
  border: 1px black solid;
  margin-left: 1px;
  text-align: center;
  width: 30%;
}
.progress {
  border: 1px black solid;
  margin-left: 1px;
  text-align: center;
  width: 40%;
}
.last-update {
  border: 1px black solid;
  margin-left: 1px;
  text-align: center;
  width: 30%;
}
.update-button-area {
  border: 1px black solid;
  margin-left: 1px;
  text-align: center;
  width: 10%;
}
#overlay{
  z-index:1;
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background-color:rgba(0,0,0,0.7);
  display: flex;
  align-items: center;
  justify-content: center;
}
#modal-content{
  text-align: left;
  padding: 0px 10px 10px 10px;
  border-radius: 10px;
}
#modal-area{
  margin-left: auto;
  margin-right: auto;
  position: relative;
  /* left:0px;
  top:0px; */
  max-height: 75%;
  overflow: scroll;
  z-index:5;
  width:90%;
  border-radius: 10px;
  background:#fff;
}
#window {
  z-index:5;
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  /* pointer-events:none; */
  display: flex;
  align-items: center;
  justify-content: center;
}
.create-at{
  margin-left: 5px;
  padding-left: 5px;
  border-left: 2px solid;
}
</style>
