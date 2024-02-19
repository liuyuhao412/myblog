<template>
  <div class="wrapper">
    <div class="navigation">
      <headerVue></headerVue>
    </div>
    <contentVue class="content"></contentVue>
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

.navigation {
  flex: 0;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
}
.content {
  flex: 1;
  margin-top: 52px;
  min-height: 1800px;
}
</style>
