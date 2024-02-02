<template>
  <div class="header">
    <div class="header-left">
      <span class="iconfont logo">&#xe600;</span>
      <div class="title">水墨轩</div>
    </div>
    <div class="header-right">
      <div class="nav-item">首页</div>
      <div class="nav-item">社区</div>
      <div class="nav-item">我的</div>
      <div class="user-login-in" @click="login">登录</div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const login = (): void => {
  console.log("login");
};
</script>

<style scoped>
@import "@/assets/css/iconfont.css";

.header {
  height: 40px;
  padding: 5px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgba(92, 109, 126, 0.2);
  position: fixed;
  width: 100%;  
  top: 0;
}

.header-left {
  width: 100px;
  margin-left: 60px;
  display: flex;
  align-items: center;
}

.header-right {
  width: 260px;
  margin-right: 10px;
  display: flex;
}

.nav-item {
  width: 60px;
  text-align: center;
  line-height: 40px;
}

.nav-item:hover {
  background-color: rgba(132, 139, 145, 0.8); /* 鼠标悬停时的背景颜色 */
}

.logo {
  font-size: 20px;
  margin-right: 10px;
}

.title {
  font-size: 20px;
  font-weight: bold;
}

.user-login-in {
  width: 40px;
  height: 40px;
  margin: 0 20px;
  background-color: rgba(132, 139, 145, 0.5);
  border-radius: 50%;
  font-size: 16px;
  text-align: center;
  line-height: 40px;
  cursor: pointer;
}
</style>
