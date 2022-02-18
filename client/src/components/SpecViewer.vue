<template>
  <input type="file" @change="uploadWav" />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { getWaveform } from "../utils/utils";

export default defineComponent({
  setup() {
    const wav = ref(null);
    const uploadWav = async (e: any) => {
      const file = e.target.files[0];
      const formData = new FormData();
      formData.append("file", file);
      wav.value = await getWaveform(formData);
    };
    return {
      uploadWav,
    };
  },
});
</script>
