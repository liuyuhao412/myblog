<template>
  <div class="about-layout">
    <Header />
    <el-container class="main-container">
      <el-main>
        <div class="content">
          <h2>修改个人信息</h2>
          <el-form :model="Updateform" ref="formRef" label-width="120px">
            <el-form-item label="用户名">
              <el-input
                v-model="Updateform.username"
                placeholder="请输入用户名"
                readonly
              />
            </el-form-item>
            <el-form-item label="姓名">
              <el-input v-model="Updateform.name" placeholder="请输入姓名" />
            </el-form-item>
            <el-form-item label="邮箱">
              <el-input v-model="Updateform.email" placeholder="请输入邮箱" />
            </el-form-item>
            <el-form-item label="头像">
              <el-upload
                class="avatar-uploader"
                action="http://127.0.0.1:5000/upload-avatar"
                :show-file-list="false"
                :before-upload="handleAvatarChange"
                :on-change="handleAvatarChange"
              >
                <img
                  :src="'http://localhost:5000' + Updateform.avatar"
                  class="avatar"
                  alt="头像"
                />
              </el-upload>
            </el-form-item>
            <el-form-item label="简介">
              <el-input
                type="textarea"
                v-model="Updateform.info"
                placeholder="请输入简介"
              />
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm">保存</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-main>
    </el-container>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from "@/components/myBlog/headerView.vue";
import Footer from "@/components/myBlog/footerView.vue";
import { get_user_profile, update_profile } from "@/api/profile";
import { ref, computed, onMounted } from "vue";
import { ElMessage } from "element-plus";
import { useRouter } from "vue-router";
import { useStore } from "vuex";

const store = useStore();
const router = useRouter();
const isLogin = computed(() => store.getters.isLogin);

const Updateform = ref({
  username: "",
  name: "",
  email: "",
  avatar: "",
  info: "",
});

onMounted(async () => {
  if (isLogin.value) {
    try {
      const response = await get_user_profile();
      const data = response.data.data;
      if (response.status === 200) {
        Updateform.value = {
          username: data.username,
          name: data.name,
          email: data.email,
          avatar: data.avatar,
          info: data.info,
        };
      }
    } catch (error) {
      console.error("获取用户信息失败");
    }
  }
});

const handleAvatarChange = (file: any) => {
  if (file.status === "success") {
    Updateform.value.avatar = file.response.avatarUrl;
  } else if (file.status === "error") {
    console.error("头像上传失败");
  }
};
const submitForm = async () => {
  console.log("保存个人信息", Updateform.value);
  try {
    const response = await update_profile(
      Updateform.value.username,
      Updateform.value.name,
      Updateform.value.email,
      Updateform.value.avatar,
      Updateform.value.info
    );
    if (response.status === 200) {
      ElMessage({
        message: response.data.message,
        type: "success",
        duration: 1000,
      });
      setTimeout(() => {
        router.push("/index");
      }, 1000);
    } else {
      ElMessage({
        message: response.data.message,
        type: "error",
        duration: 1000,
      });
    }
  } catch (error) {
    console.error("获取用户信息失败");
  }
};
</script>

<style scoped>
.about-layout {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
}

.main-container {
  display: flex;
  margin-top: 20px;
}

.content {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  font-size: 1.1rem;
  line-height: 1.8;
}

.content h2 {
  font-size: 2rem;
  margin-bottom: 20px;
  color: #333;
}

.avatar-uploader {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
  background: #f5f5f5;
  position: relative;
  border: 2px solid #ddd;
  cursor: pointer;
  /* Show pointer cursor to indicate clickability */
}

.avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
