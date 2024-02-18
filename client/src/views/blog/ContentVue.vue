<template>
  <div class="wrapper">
    <router-view></router-view>
  </div>
</template>

<script lang="ts" setup></script>
<style scoped>
.wrapper {
  background-color: #f0f0f0;
  width: 1200px;
  margin: 0 auto;
}

@media screen and (max-width: 500px) {
  .wrapper {
    background-color: #ffffff;
    width: 90vw;
    padding: 0 auto;
  }
}
</style>
