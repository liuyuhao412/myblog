<template>
  <div class="wrapper">
    <div class="form-wrapper">
      <div class="title-wrapper">
        <h1>登录</h1>
      </div>
      <el-form :model="loginForm" label-width="50px">
        <el-form-item label="账号">
          <el-input v-model="loginForm.username" />
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="loginForm.password" type="password" />
        </el-form-item>
        <el-form-item>
          <div class="signin-text">若无账号,请 <span @click="toRegister">注册</span></div>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="login">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { loginUser } from "@/api/auth";
import { ElMessage } from "element-plus";

const store = useStore();
const router = useRouter();

const loginForm = ref({
  username: "",
  password: "",
});

const toRegister = () => {
  router.push("/register_view");
};

const login = async () => {
  try {
    const response = await loginUser(loginForm.value.username, loginForm.value.password);
    if (response.status == 200) {
      localStorage.setItem("token", response.data.token);
      store.dispatch("login");
      ElMessage({
        message: response.data.message,
        type: "success",
        duration: 1000,
      });
      setTimeout(() => {
        router.push("/index");
      }, 1000);
    } else {
      ElMessage.error(response.data.message || "登录失败。");
    }
  } catch (error) {
    if (error.response) {
      // 服务器返回了响应，但状态码是错误的
      const errorMessage =
        error.response.data.message || "登录失败。请检查您的账号或密码。";
      ElMessage.error(errorMessage);
    } else {
      // 网络错误或其他问题
      ElMessage.error("登录失败。请稍后再试。");
    }
  }
};
</script>

<style scoped>
.wrapper {
  width: 100%;
  min-height: 100vh;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-image: url("@/assets/images/login_bkg.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.form-wrapper {
  width: 100%;
  max-width: 300px;
  padding: 40px 20px;
  background-color: rgba(240, 240, 240, 0.8);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.title-wrapper {
  text-align: center;
  margin-bottom: 20px;
}

.signin-text {
  text-align: center;
}

.signin-text span {
  color: #409eff;
  cursor: pointer;
  transition: color 0.3s;
}

.signin-text span:hover {
  color: #66b1ff;
}

.el-form-item {
  margin-bottom: 20px;
}

.el-button--primary {
  width: 120px;
  padding: 0 20px;
}

@media (max-width: 480px) {
  .form-wrapper {
    width: 90%;
  }
}
</style>
