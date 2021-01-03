<template>
  <v-dialog :value="active" hide-overlay persistent width="300">
    <v-card color="primary" dark>
      <v-card-text>
        アップロード中…
        <v-progress-linear indeterminate color="white" class="mb-0" />
      </v-card-text>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  props: {
    active: Boolean,
  },
  watch: {
    active(val) {
      if (!val) return
      setTimeout(() => this.$emit('upload-end'), 400)
    },
  },
}
</script>

<style></style>
