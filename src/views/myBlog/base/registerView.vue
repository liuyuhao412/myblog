<template>
    <div class="wrapper">
        <div class="form-wrapper">
            <div class="title-wrapper">
                <h1>注册</h1>
            </div>
            <el-form :model="registerForm" label-width="80px">
                <el-form-item label="账号" prop="username">
                    <el-input v-model="registerForm.username" />
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input v-model="registerForm.password" type="password" />
                </el-form-item>
                <el-form-item label="确认密码" prop="confirmPassword">
                    <el-input v-model="registerForm.confirmPassword" type="password" />
                </el-form-item>
                <el-form-item>
                    <div class="signup-text">
                        若有账号请 <span @click="toLogin">登录</span>
                    </div>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="register">注册</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { registerUser } from '@/types'

const router = useRouter();

const registerForm = ref < registerUser > ({
    username: '',
    password: '',
    confirmPassword: ''
});

const toLogin = () => {
    router.push("/login_view");
};

const register = () => {
    router.push("/login_view");
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
    max-width: 400px;
    padding: 40px 20px;
    background-color: rgba(240, 240, 240, 0.8);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

.title-wrapper {
    text-align: center;
    margin-bottom: 20px;
}

.signup-text {
    text-align: center;
}

.signup-text span {
    color: #409EFF;
    cursor: pointer;
    transition: color 0.3s;
}

.signup-text span:hover {
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
