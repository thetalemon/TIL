<template>
  <v-container>
    <v-layout text-xs-center wrap>
      <v-flex xs12 mb-5>
        <v-card dark color="primary">
          <v-card-text class="px-0">Welcome to theta-portfoilo</v-card-text>
        </v-card>
      </v-flex>

      <v-flex xs12 mb-5>
        <!-- <h2 background="#00fffff">{{skill.skillName}}</h2> -->
        <v-card dark color="primary">
        <v-layout>
          <p>
          <table width = "100%" v-for="(skill, key, index) in Skills" :key="index" align="left">
            <!-- <table v-for="(skill, key, index) in Skills" :key="index" align="left"> -->
              <tr><th colspan="2"> <h2>{{skill.skillName}}</h2> </th></tr>
              <tbody width="100%" v-for="(content, key2, index2) in skill.contents"
                :key="index2"
                align="left">
                <tr>
                  <td width="30%"> <a @click="active(key,key2)">{{content.name}}</a> </td>
                  <td> {{content.term}} </td>
                </tr>
                <tr v-if=content.isActive><td colspan="2"> {{content.despcript}} </td></tr>
            </tbody>
          </table>
        </p>
        </v-layout>
       </v-card>
      </v-flex>

      <v-flex xs12 mb-5>
        <v-card dark color="primary">
        <v-layout>
          <table>
            <tr><th colspan="2"> <h2>趣味</h2> </th></tr>
            <tr v-for="(hobby, key, index) in Hobby" :key="index" align="left">
              <td width="30%"> <!-- <a @click="active(key,key2)"> -->{{hobby.hobbyName}}<!-- </a>--> </td>
              <td> {{hobby.despcript}} </td>
            </tr>
          </table>
        </v-layout>
       </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      Skills: [
        {
          skillName : '言語・フレームワークなど',
          contents: [
            {
              name: 'Java',
              term: '★★★',
              despcript: '業務利用。SpringFrameworkを利用して、APIやバッチ１本作れる。SpringBatchの使用経験もchunk,tasklet両方有。',
              isActive: false
            },
            {
              name: 'Python',
              term: '★★★',
              despcript: '研究・趣味利用。Chainerを利用した画像・音楽マッチングシステムの作成に利用。CSVの操作、OpenCVを利用した画像処理、librosaを利用した楽曲解析、pretty_midiを利用したmidi生成、Chainerを利用した学習モデルの作成ができる。また、バックエンド用としてFlaskの実装も行ったことがある。',
              isActive: false
            },
            {
              name: 'ShellScript',
              term: '★★★',
              despcript: '業務利用。AWKコマンド使って文書の体裁チェックが作れる。',
              isActive: false
            },
            {
              name: 'C++',
              term: '★★',
              despcript: '研究利用。動画情報をに基づいた自動作曲システムの作成に利用。OpenCVを利用した画像・動画解析、おーぷんMIDIを利用したMIDIの作成ができる',
              isActive: false
            },
            {
              name: 'PHP',
              term: '★',
              despcript: '授業履修。基礎をやったことがある程度',
              isActive: false
            },
            {
              name: 'HTML4',
              term: '★',
              despcript: '過去に個人でホームページを作成した。フレームなどがわかる程度。',
              isActive: false
            },
            {
              name: 'CSS',
              term: '★',
              despcript: '過去に個人でホームページを作成した。基礎的なことがわかる程度。',
              isActive: false
            },
          ]
        },
        {
          skillName: '周辺技術',
          contents: [
            {
              name: 'git',
              term: '★★★',
              despcript: '業務利用。基礎的なことはできる。',
              isActive: false
            },
            {
              name: 'SQL',
              term: '★★',
              despcript: '業務利用。入れ子や結合が利用できる。主に利用していたのはOracleDB。',
              isActive: false
            },
            {
              name: 'Docker',
              term: '★★',
              despcript: '趣味利用s。Vue.js + Flask + uwsgi + Nginxで作成した個人サイトをサーバ上で手軽に展開できるような環境を構築。また、自PCとサーバ上で同様の環境で開発できるような環境も作成した。',
              isActive: false
            },
            {
              name: 'Ansible',
              term: '★',
              despcript: '業務利用。利用・修正をしたことがある。読んで修正ができる程度。',
              isActive: false
            }
          ]
        },
        {
          skillName: 'その他',
          contents: [
            {
              name: '英語',
              term: '★★',
              despcript: 'TOEIC730点。',
              isActive: false
            },
            {
              name: 'タイ語',
              term: '★★★',
              despcript: 'スピーキング・リスニングのみ。日常会話程度。海外ドラマの日本語字幕からタイ語への同時通訳ができる程度。',
              isActive: false
            }
          ]
        }
      ],
      Hobby: [
        {
          hobbyName: '写真',
          despcript: 'ミラーレス一眼で主に風景を。被写体としては空・鉄塔・線路・建機などが好き。',
          url: '写真',
        },
        {
          hobbyName: '創作',
          despcript: '主にイラストと小説。世界観と衣装・キャラクターを考えるのが好き。',
          url: '写真',
        },
        {
          hobbyName: '読書',
          despcript: '2019年4月末頃から週１冊で読んでいる。最近は経済系をメインに読んでいる。',
          url: '写真',
        },
        {
          hobbyName: '映画・アニメ鑑賞',
          despcript: '人類が滅亡の危機に直面する映画か、親子愛モノが好き。最近見た中だとアベンジャーズが激推し。アニメはSHIROBAKOやNEW GAME!など、目標に向かって頑張るのが好き。',
          url: '写真',
        },
        {
          hobbyName: '音楽鑑賞',
          despcript: 'ポップスからロックから洋楽まで幅広く好き。最近の推しは[ALEXANDROS]とフレデリック。',
          url: '写真',
        }
      ]
    }),
    methods: {
      active (key1,key2) {
        this.Skills[key1].contents[key2].isActive = !this.Skills[key1].contents[key2].isActive
      }
    }
  }
</script>

<style>
table{
  width: 100%;
}

td,th{
  padding: 10px 30px;
}
th{
  background-color: #0099ff;
}
td {
  background-color: #ffffff;
  color: #000000;
}

</style>
