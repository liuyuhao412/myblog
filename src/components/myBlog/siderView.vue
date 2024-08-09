<template>
  <el-aside width="300px">
    <div class="sidebar">
      <!-- 登录状态 -->
      <div v-if="isLogin" class="profile">
        <img :src="userInfo.avatar" alt="头像" class="profile-avatar" />
        <h3>{{ userInfo.username }}</h3>
        <p class="profile-info">{{ userInfo.info }}</p>
        <div class="stats">
          <div class="stat-item">
            <span>{{ userInfo.articleCount }}</span>
            <p>日志</p>
          </div>
          <div class="stat-item">
            <span>{{ userInfo.tagCount }}</span>
            <p>标签</p>
          </div>
        </div>
        <div class="tags">
          <h3>标签云</h3>
          <div class="tag-list">
            <el-tag v-for="userTag in userTags" :key="userTag" class="tag-item">
              {{ userTag }}
            </el-tag>
          </div>
        </div>
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
        <div class="tags">
          <h3>标签云</h3>
          <div class="tag-list">
            <el-tag v-for="defaultTag in defaultTags" :key="defaultTag" class="tag-item">
              {{ defaultTag }}
            </el-tag>
          </div>
        </div>
      </div>


    </div>
  </el-aside>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { UserInfo } from "@/utils/type";
import { useStore } from 'vuex';

const store = useStore();
const isLogin = computed(() => store.getters.isLogin);

const userInfo = ref<UserInfo>({
  username: '用户名',
  avatar: 'https://via.placeholder.com/100',
  email: 'user@example.com',
  info: '这是一段个人简介。',
  articleCount: 10,
  tagCount: 5,
});

const userTags = ref<string[]>([
  '标签一', '标签二', '标签三', '标签四', '标签五',
  '标签六', '标签七', '标签八', '标签九', '标签十',
  '标签11', '标签12', '标签13', '标签14', '标签15',
]);

const defaultTags = ref<string[]>([
  '默认一', '默认二', '默认三', '默认四', '默认五'
]);
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
