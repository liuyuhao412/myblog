<template>
  <div class="header">
    <div class="header-item-left">
      <span class="iconfont logo">&#xe600;</span>
      <div class="title">水墨轩</div>
    </div>

    <div class="header-item-right">
      <div class="login-btn" @click="login" v-if="showLogin">登录</div>
      <input type="checkbox" v-model="isMenuOpen" class="menu" />
      <span class="iconfont menu-icon" @click="openMenu">&#xe609;</span>
      <div class="nav-menu" :class="{ open: isMenuOpen }">
        <div class="nav-item" @click="closeMenu">首页</div>
        <div class="nav-item" @click="closeMenu">社区</div>
        <div class="nav-item" @click="closeMenu">我的</div>
      </div>
    </div>
  </div>
  <DialogVue :dialogTitle="dialogTitle" v-model="dialogVisible">
    <el-input placeholder="请输入用户名" />
    <el-input placeholder="密码在此完成" />
    <el-button type="info">登录</el-button>
  </DialogVue>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import DialogVue from "@/components/DialogVue.vue";
const showLogin = ref<boolean>(true);
const isMenuOpen = ref<boolean>(false);
//登录弹窗
const dialogVisible = ref<boolean>(false);
const dialogTitle = ref<string>("");

const login = (): void => {
  dialogVisible.value = true;
  dialogTitle.value = "登录";
  console.log("登录成功");
  showLogin.value = false;
};

const openMenu = (): void => {
  isMenuOpen.value = !isMenuOpen.value;
};

const closeMenu = (): void => {
  isMenuOpen.value = !isMenuOpen.value;
};
</script>

<style scoped>
@import "@/assets/css/iconfont.css";
.header {
  padding: 10px 0;
  background-color: #5f5a5a;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: fixed;
  width: 100%;
  top: 0;
}

.header-item-left {
  display: flex;
  align-items: center;
  margin-left: 1rem;
}

.logo {
  font-size: 24px;
  margin-right: 10px;
}

.title {
  font-size: 24px;
}
.header-item-right {
  display: flex;
  align-items: center;
  margin-right: 1rem;
}
.login-btn {
  cursor: pointer;
  background-color: #71d8b4;
  color: #5f5a5a;
  font-size: 16px;
  padding: 4px 12px;
  border-radius: 5px;
  margin-right: 1rem;
}

.menu {
  display: none;
}
.menu-icon {
  font-size: 24px;
  cursor: pointer;
  user-select: none; /* 禁用用户选中效果 */
}

.nav-menu {
  display: none;
}

.nav-menu.open {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 50px; /* 距离顶部的距离，根据实际需要调整 */
  right: 10px;
  background-color: #5f5a5a;
  padding: 10px 20px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  border-radius: 5px;
}

.nav-item {
  margin-bottom: 10px;
  cursor: pointer;
  color: #fff;
  font-size: 16px;
}

.nav-item:last-child {
  margin-bottom: 0;
}

.nav-item:hover {
  color: #ffd700;
}

/* 添加媒体查询，适应小屏幕 */
@media screen and (max-width: 600px) {
}
</style>
