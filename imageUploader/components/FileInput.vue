<template>
  <div>
    <v-row
      class="text-center"
      @dragover.prevent
      @dragenter="onDragEnter"
      @dragleave="onDragLeave"
      @drop="onDrop"
    >
      <v-file-input
        v-model="file"
        class="mt-10 mx-5"
        label="クリックまたはドラッグ＆ドロップでファイルを選択"
        outlined
        filled
        small-chips
        prepend-icon="mdi-camera"
        accept=".png,.jpg"
        @change="onChange()"
      />
    </v-row>
  </div>
</template>

<script>
// 参考：https://www.ultra-noob.com/blog/2020/2020-06-19-%E3%80%90Vue_js%E3%80%91CSS%E3%81%AA%E3%81%97%E3%81%A7%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E3%83%89%E3%83%A9%E3%83%83%E3%82%B0%E3%82%A2%E3%83%B3%E3%83%89%E3%83%89%E3%83%AD%E3%83%83%E3%83%97%E3%81%A7%E8%BF%BD%E5%8A%A0%E3%81%99%E3%82%8B%EF%BC%81%E3%80%90Vuetify%E3%80%91/
export default {
  data: () => ({
    file: undefined,
    isDragging: false,
    dragCount: 0,
  }),
  methods: {
    onDrop(e) {
      e.preventDefault()
      e.stopPropagation()
      this.isDragging = false
      const _files = e.dataTransfer.files
      this.file = _files[0]
    },
    onDragEnter(e) {
      e.preventDefault()
      this.isDragging = true
      this.dragCount++
    },
    onDragLeave(e) {
      e.preventDefault()
      this.dragCount--
      if (this.dragCount <= 0) {
        this.isDragging = false
      }
    },
    onChange() {
      this.$emit('change-file', this.file)
    },
  },
}
</script>
