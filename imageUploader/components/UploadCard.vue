<template>
  <v-content>
    <v-card>
      <v-layout justify-center>
        <v-card-title class="headline text-center">
          画像アップローダー
        </v-card-title>
      </v-layout>
      <v-layout justify-center>
        <v-card-subtitle>対応ファイル：JPG,PNG</v-card-subtitle>
      </v-layout>
      <file-input @change-file="onChangeFile($event)" />
      <v-layout justify-center>
        <v-card-actions>
          <v-btn
            :disabled="uploading || !file"
            :loading="uploading"
            outlined
            text
            large
            @click="onClick()"
          >
            upload!
          </v-btn>
        </v-card-actions>
      </v-layout>
      <v-img v-show="uploadedImage" :src="uploadedImage" class="mx-5" />
    </v-card>
  </v-content>
</template>
<script>
import FileInput from '~/components/FileInput.vue'

export default {
  components: {
    FileInput,
  },
  props: {
    uploading: Boolean,
  },
  data() {
    return {
      uploadedImage: undefined,
      file: undefined,
    }
  },
  methods: {
    onChangeFile(e) {
      if (e) {
        let reader = new FileReader()
        reader.onload = (e) => {
          this.uploadedImage = e.target.result
        }
        reader.readAsDataURL(e)
      }
      this.file = e
    },
    onClick() {
      this.$emit('click-upload', this.file)
    },
  },
}
</script>
