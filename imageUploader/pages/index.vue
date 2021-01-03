<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <div class="text-center">
        <upload-card
          v-if="!uploaded"
          :uploading="uploading"
          @click-upload="onClickUpload($event)"
        />
        <upload-end v-if="uploaded" />
        <upload-dialog :active="uploading" @upload-end="onUploadEnd()" />
      </div>
    </v-col>
  </v-row>
</template>

<script>
import UploadCard from '~/components/UploadCard.vue'
import UploadDialog from '~/components/UploadDialog.vue'
import UploadEnd from '~/components/UploadEnd.vue'

export default {
  components: {
    UploadCard,
    UploadDialog,
    UploadEnd,
  },
  data() {
    return {
      uploading: false,
      uploaded: false,
    }
  },
  methods: {
    onClickUpload() {
      this.uploading = true
    },
    onUploadEnd() {
      this.uploading = false
      this.uploaded = true
    },
  },
}
</script>
