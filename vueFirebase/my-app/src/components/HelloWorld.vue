<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >

      <v-flex mb-4>
        <v-card dark color="primary">
          <v-card-text class="px-0">Welcome to theta-portfoilo</v-card-text>
        </v-card>
      </v-flex>

      <v-flex
        xs12
        mb-5
      >
        <h2 class="headline font-weight-bold mb-3">Skills</h2>

        <v-card dark color="primary">
        <v-layout >
            <tbody>
              <tr v-for="(skill, key, index) in skills"
                :key="index"
                align="left">
                <td> {{skill.skillName}} </td>
                <td> {{skill.despcript}} </td>
              </tr>
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
      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader'
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify'
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify'
        }
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com'
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com'
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuetifyjs.com'
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs'
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify'
        }
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer'
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/layout/pre-defined'
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions'
        }
      ],
      skills: [
        {
          skillName: 'Java',
          despcript: '業務利用。SpringFrameworkを利用して、APIやバッチ１本作れる。'
        },
        {
          skillName: 'Python',
          despcript: 'Chainerを利用して画像判定システムを作成できる。'
        },
        {
          skillName: 'ShellScript',
          despcript: '業務利用。AWKコマンド使って文書の体裁チェックが作れる。'
        }
      ]
    })
  }
</script>

<style>
td, th {
padding: 10px 20px;
}

</style>
