<template>
  <div class="header">
    <div class="header-item-left">
      <span class="iconfont logo">&#xe600;</span>
      <div class="title">水墨轩</div>
    </div>

    <div class="header-item-right">
      <div class="item-div">
        <span class="iconfont item-div-icon">&#xe646;</span>
        <router-link to="/index_home" class="router-link">主页</router-link>
      </div>
      <div class="item-div" v-if="!isLogin">
        <span class="iconfont item-div-icon">&#xe601;</span>
        <router-link to="/index_home" class="router-link">分类</router-link>
      </div>
      <div class="item-div" v-if="!isLogin">
        <span class="iconfont item-div-icon">&#xe608;</span>
        <router-link to="/index_home" class="router-link">说说</router-link>
      </div>
      <div class="item-div" v-if="!isLogin">
        <span class="iconfont item-div-icon">&#xe614;</span>
        <router-link to="/index_home" class="router-link">我的</router-link>
      </div>
      <div class="login-btn" @click="login" v-if="isLogin">登录</div>
      <div class="login-btn" @click="exit" v-if="!isLogin">退出</div>
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
      router.push({ path: "/index_home" });
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
  margin-left: 60px;
}

.logo {
  font-size: 30px;
  margin-right: 10px;
}

.title {
  font-size: 28px;
}
.header-item-right {
  display: flex;
  align-items: center;
  margin-right: 20px;
}
.login-btn {
  cursor: pointer;
  background-color: #71d8b4;
  color: #000;
  font-size: 18px;
  padding: 6px 12px;
  border-radius: 5px;
}

.login-btn:active {
  color: #fcc6ab;
}

.item-div {
  font-size: 18px;
  color: #5f5a5a;
  margin-right: 20px;
  padding: 6px 12px;
  border-radius: 5px;
}
.item-div:hover {
  background-color: #71d8b4;
}

.router-link {
  color: #000;
}

.item-div-icon {
  font-size: 16px;
  color: #000;
  font-weight: bold;
  margin-right: 5px;
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
</style>
