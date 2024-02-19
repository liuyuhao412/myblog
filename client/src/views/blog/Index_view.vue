<template>
  <div class="wrapper">
    <headerVue></headerVue>
    <contentVue></contentVue>
    <footerVue></footerVue>
  </div>
</template>

<script lang="ts" setup>
import headerVue from "@/views/blog/headerVue.vue";
import contentVue from "@/views/blog/contentVue.vue";
import footerVue from "@/views/blog/footerVue.vue";
</script>
<style scoped>
.wrapper {
  display: flex;
  flex-direction: column;
}
</style>
