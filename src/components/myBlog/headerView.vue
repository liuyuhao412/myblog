<template>
  <el-header class="header">
    <h1>myBlog</h1>
    <el-menu mode="horizontal" class="menu" :default-active="activeIndex" @select="menuSelect">
      <el-menu-item index="/">首页</el-menu-item>
      <el-menu-item v-if="isLogIn" index="/categories">分类</el-menu-item>
      <el-menu-item v-if="isLogIn" index="/article/edit">写文章</el-menu-item>
      <el-menu-item index="/about">关于我</el-menu-item>
    </el-menu>
    <el-input class="search-input" placeholder="请输入搜索内容" clearable></el-input>
    <el-button type="primary" @click="handleLogin">{{ isLogIn ? '退出' : '登录' }}</el-button>
  </el-header>
</template>

<script setup lang="ts">
import { computed, ref, watch } from 'vue';
import { useStore } from 'vuex';
import { useRouter, useRoute } from 'vue-router';

const store = useStore();
const route = useRoute();
const router = useRouter();

const activeIndex = ref<string>(route.path);
const isLogIn = computed(() => store.getters.isLogin);

const menuSelect = (index: string) => {
  activeIndex.value = index;
  router.push(index);
};

const handleLogin = () => {
  if (isLogIn.value) {
    store.dispatch('logout');
  } else {
    router.push('/login_view');
  }
};

watch(() => route.path, (newPath) => {
  activeIndex.value = newPath;
});
</script>

<style scoped>
.header {
  background: linear-gradient(90deg, #4169E1, #1E90FF);
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  border-radius: 12px 12px 0 0;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.header h1 {
  font-size: 2.2rem;
  font-weight: bold;
  margin: 0;
}

.header h1:hover {
  color: #dfe6ff;
}

.menu {
  flex-grow: 1;
  margin-left: 40px;
  font-size: 1.6rem;
}

.el-menu-item {
  transition: color 0.3s;
}

.el-menu-item:hover {
  color: #dfe6ff;
}

.search-input {
  max-width: 300px;
  margin: 0 2em;
  border-radius: 6px;
}

.search-input:focus {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
}
</style>