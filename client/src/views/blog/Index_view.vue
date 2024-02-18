<template>
  <div class="wrapper">
    <div class="navigation">
      <NavigationVue></NavigationVue>
    </div>
    <ContentVue class="content"></ContentVue>
  </div>
</template>

<script lang="ts" setup>
import NavigationVue from "@/views/blog/NavigationVue.vue";
import ContentVue from "@/views/blog/ContentVue.vue";
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
  margin-top: 50px;
}
</style>
