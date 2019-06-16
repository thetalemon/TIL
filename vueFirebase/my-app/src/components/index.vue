<template>
  <v-container>
    <v-layout text-xs-center wrap>
      <v-flex mb-4>
        <v-card dark color="primary">
          <v-card-text class="px-0">Welcome to theta-portfoilo</v-card-text>
        </v-card>
      </v-flex>

      <v-flex xs12 mb-5>
        <h2 class="headline font-weight-bold mb-3">Skills</h2>

        <v-card dark color="primary">
        <v-layout>
          <table>
            <tbody v-for="(skill, key, index) in Skills" :key="index" align="left">
              <tr><th colspan="2"> {{skill.skillName}} </th></tr>
              <tbody v-for="(content, key2, index2) in skill.contents"
                :key="index2"
                align="left">
                <tr>
                  <td> {{content.name}}</td>
                  <!-- <td> <a @click="active(content)">{{content.name}}</a> </td> -->
                  <td> {{content.term}} </td>
                  <td> {{content.despcript}} </td>
                  <!-- <tr v-if=content.isActive><td colspan="2"> {{content.despcript}} </td></tr> -->
                </tr>
              </tbody>
            </tbody>
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
      isActive: true,
      Skills: [
        {
          skillName : '言語・フレームワークなど',
          contents: [
            {
              name: 'Java',
              term: '★★★',
              despcript: '業務利用。SpringFrameworkを利用して、APIやバッチ１本作れる。SpringBatchの使用経験もchunk,tasklet両方有。',
              isActive: true
            },
            {
              name: 'Python',
              term: '★★★',
              despcript: '研究利用。Chainerを利用した画像・音楽マッチングシステムの作成に利用。CSVの操作、OpenCVを利用した画像処理、librosaを利用した楽曲解析、pretty_midiろ利用したmidi生成、Chainerを利用した学習モデルの作成ができる'
            },
            {
              name: 'ShellScript',
              term: '★★★',
              despcript: '業務利用。AWKコマンド使って文書の体裁チェックが作れる。'
            },
            {
              name: 'C++',
              term: '★★',
              despcript: '研究利用。動画情報をに基づいた自動作曲システムの作成に利用。OpenCVを利用した画像・動画解析、おーぷんMIDIを利用したMIDIの作成ができる'
            },
            {
              name: 'PHP',
              term: '★',
              despcript: '授業履修。基礎をやったことがある程度'
            },
          ]
        },
        {
          skillName: '周辺技術',
          contents: [
            {
              name: 'git',
              term: '★★★',
              despcript: '業務利用。基礎的なことはできる。'
            },
            {
              name: 'SQL',
              term: '★★',
              despcript: '業務利用。入れ子や結合が利用できる。'
            }
          ]
        },
        {
          skillName: 'その他',
          contents: [
            {
              name: '英語',
              term: '★★',
              despcript: 'TOEIC730点'
            },
            {
              name: 'タイ語',
              term: '★★★',
              despcript: 'スピーキング・リスニングのみ。日常会話程度。'
            }
          ]
        }
      ]
    }),
    // methods: {
    //   active (flg) {
    //     flg = !flg
    //   }
    // }
  }
</script>

<style>
td,th{
  padding: 10px 20px;
}
th{
  background-color: #0099ff;
}
td {
  background-color: #ffffff;
  color: #000000;
}

</style>
