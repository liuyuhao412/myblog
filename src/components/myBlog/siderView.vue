<template>
  <el-aside width="300px">
    <div class="sidebar">
      <!-- 登录状态 -->
      <div v-if="isLogin" class="profile">
        <img
          :src="'http://localhost:5000' + userInfo.avatar"
          alt="头像"
          class="profile-avatar"
        />
        <h3>{{ userInfo.username }}</h3>
        <p class="profile-info">{{ userInfo.info }}</p>
        <div class="stats">
          <div class="stat-item">
            <span>{{ userInfo.articleCount }}</span>
            <p>日志</p>
          </div>
        </div>
        <el-button type="primary" class="edit-btn" @click="editProfile"
          >编辑资料</el-button
        >
      </div>

      <!-- 未登录状态 -->
      <div v-else class="profile">
        <img src="https://via.placeholder.com/100" alt="头像" class="profile-avatar" />
        <h3>请登录</h3>
        <p class="profile-info">欢迎来到博客！请登录以查看个人信息。</p>
        <div class="stats">
          <div class="stat-item">
            <span>0</span>
            <p>日志</p>
          </div>
          <div class="stat-item">
            <span>0</span>
            <p>标签</p>
          </div>
        </div>
      </div>
    </div>
  </el-aside>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { UserInfo } from "@/utils/type";
import { useStore } from "vuex";
import { get_user_profile } from "@/api/profile";
import { useRouter } from "vue-router";

const store = useStore();
const router = useRouter();
const isLogin = computed(() => store.getters.isLogin);

const userInfo = ref<UserInfo>({
  username: "用户名",
  avatar: "https://via.placeholder.com/100",
  email: "user@example.com",
  info: "这是一段个人简介。",
  articleCount: 0,
});

onMounted(async () => {
  if (isLogin.value) {
    try {
      const response = await get_user_profile();
      if (response.status == 200) {
        userInfo.value = response.data.data;
      }
    } catch (error) {
      console.error("获取用户信息失败");
    }
  }
});

const editProfile = () => {
  // 跳转到编辑个人资料页面
  console.log("编辑个人资料");
  router.push("/edit-profile");
};
</script>

<style scoped>
.sidebar {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile h3,
.tags h3 {
  font-size: 1.6rem;
  color: #333;
  margin-bottom: 10px;
}

.profile {
  text-align: center;
  padding: 20px;
  border-radius: 12px;
}

.profile p {
  font-size: 1rem;
  color: #666;
  line-height: 1.6;
}

.profile-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 10px;
  border: 3px solid #fff;
  transition: transform 0.3s;
}

.profile-avatar:hover {
  transform: scale(1.1);
}

.profile-info {
  margin: 10px 0;
  font-size: 1rem;
  color: #ccc;
}

.stats {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.stat-item {
  flex: 1;
  text-align: center;
}

.stat-item span {
  display: block;
  font-size: 1.2rem;
  font-weight: bold;
}

.stat-item p {
  margin: 0;
  font-size: 0.9rem;
  color: #aaa;
}

.edit-btn {
  margin-top: 10px;
}

.tags {
  margin-top: 20px;
}

.tags h3 {
  margin-bottom: 10px;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.tag-item {
  cursor: pointer;
  font-size: 14px;
  padding: 5px 10px;
  transition: background-color 0.3s, color 0.3s;
  border-radius: 4px;
  background-color: #e8e8e8;
}

.tag-item:hover {
  background-color: #d0d0d0;
  color: #000;
}
</style>
