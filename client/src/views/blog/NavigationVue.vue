<template>
  <div class="header">
    <div class="header-item-left">
      <span class="iconfont logo">&#xe600;</span>
      <div class="title">水墨轩</div>
    </div>

    <div class="header-item-right">
      <div class="login-btn" @click="login" v-if="isLogin">登录</div>
      <div class="login-btn" @click="exit" v-if="!isLogin">退出</div>
      <input type="checkbox" v-model="isMenuOpen" class="menu" />
      <span class="iconfont menu-icon" @click="openMenu">&#xe609;</span>
      <div class="nav-menu" :class="{ open: isMenuOpen }">
        <router-link to="/home" class="nav-item" @click="closeMenu"
          >首页</router-link
        >
        <router-link to="/community" class="nav-item" @click="closeMenu"
          >社区</router-link
        >
        <router-link
          to="/my_info"
          class="nav-item"
          @click="closeMenu"
          v-if="!isLogin"
          >我的</router-link
        >
      </div>
    </div>
  </div>
  <DialogVue
    :title="title"
    :loginWidth="loginWidth"
    v-model="modelValue"
    @update:modelValue="handleDialogClose"
  >
    <el-form :model="loginForm">
      <el-input
        v-model="loginForm.Username"
        placeholder="请输入用户名"
        class="login-input"
      />
      <el-input
        v-model="loginForm.Password"
        placeholder="密码在此完成"
        type="password"
        class="login-input"
      />
      <el-button type="info" class="ok-btn" @click="loginBtn"
        >登录</el-button
      ></el-form
    >
  </DialogVue>
</template>

<script lang="ts" setup>
import DialogVue from "@/components/DialogVue.vue";
import { LoginApi } from "@/api/login";
import { ref } from "vue";
import { ElMessage, ElMessageBox } from "element-plus";
import { useRouter } from "vue-router";

interface LoginForm {
  Username: string;
  Password: string;
}

const router = useRouter();
const isLogin = ref<boolean>(true);
const isMenuOpen = ref<boolean>(false);
//登录弹窗
const modelValue = ref<boolean>(false);
const title = ref<string>("");
const loginWidth = ref<string>("300px");
const loginForm = ref<LoginForm>({
  Username: "",
  Password: "",
});

const login = (): void => {
  modelValue.value = true;
  title.value = "登录";
};

const handleDialogClose = (value: boolean): void => {
  modelValue.value = value;
};

const loginBtn = async (): Promise<void> => {
  console.log(loginForm.value);
  try {
    const res = await LoginApi(loginForm.value);
    if (res.data.code == 200) {
      ElMessage({
        message: res.data.msg,
        type: "success",
        duration: 1000,
      });
      isLogin.value = false;
      modelValue.value = false;
      loginForm.value.Username = "";
      loginForm.value.Password = "";
      router.push({ path: "/home" });
    } else {
      ElMessage({
        message: res.data.msg,
        type: "error",
        duration: 1000,
      });
    }
  } catch (error) {
    console.error("Axios request failed:", error);
  }
};
const exit = (): void => {
  ElMessageBox.confirm("您确认要退出吗？", "提示", {
    cancelButtonText: "取消",
    confirmButtonText: "确认",
    type: "warning",
  })
    .then(() => {
      ElMessage({
        type: "success",
        message: "退出成功",
        duration: 1000,
      });
      isLogin.value = true;
      router.push({ path: "/index" });
    })
    .catch(() => {
      ElMessage({
        type: "info",
        message: "取消退出",
        duration: 1000,
      });
    });
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
}

.header-item-left {
  display: flex;
  align-items: center;
  margin-left: 6rem;
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
  margin-right: 6rem;
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

.login-input {
  height: 40px;
  width: 200px;
  margin-left: 30px;
  margin-bottom: 30px;
}
.ok-btn {
  height: 40px;
  width: 120px;
  margin-left: 60px;
  margin-bottom: 10px;
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
  margin-right: 4rem;
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
@media screen and (max-width: 500px) {
  .header-item-left {
    margin-left: 1rem;
  }
  .header-item-right {
    margin-right: 1rem;
  }
  .nav-menu {
    margin-right: 0rem;
  }
}
</style>
