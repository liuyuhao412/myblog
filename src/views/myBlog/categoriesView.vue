<template>
  <div class="blog-layout">
    <Header />
    <el-container class="main-container">
      <Sidebar />
      <el-main>
        <div class="content">
          <!-- 登录状态显示用户内容 -->
          <div v-if="isLogin" class="categories-list">
            <div v-for="category in categories" :key="category.id" class="category-item">
              <a class="category-name">{{ category.name }}</a>
              <span class="category-count">({{ category.articleCount }})</span>
            </div>
          </div>
          <!-- 未登录状态显示提示信息 -->
          <div v-else class="content-message">
            <p>请登录以查看分类内容。</p>
          </div>
        </div>
      </el-main>
    </el-container>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from "@/components/myBlog/headerView.vue";
import Sidebar from "@/components/myBlog/siderView.vue";
import Footer from "@/components/myBlog/footerView.vue";
import { ref, computed } from "vue";
import { useStore } from "vuex";

const store = useStore();
const isLogin = computed(() => store.getters.isLogin);

const categories = ref([
  { id: 1, name: "技术", articleCount: 10 },
  { id: 2, name: "生活", articleCount: 5 },
  { id: 3, name: "学习", articleCount: 8 },
  { id: 4, name: "旅行", articleCount: 3 },
]);
</script>

<style scoped>
.blog-layout {
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
  gap: 20px;
}

.content {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  flex-grow: 1;
  margin-left: 10px;
  font-size: 1.1rem;
  line-height: 1.8;
  display: flex;
  justify-content: center;
}

.categories-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.category-item {
  text-align: center;
  width: 100%;
  max-width: 150px;
  cursor: pointer;
}

.category-item a {
  text-decoration: none;
  color: inherit;
  font-size: 1rem;
  transition: color 0.3s;
}

.category-item:hover {
  background-color: #b2ebf2;
  color: #004d40;
}

.category-item:hover a {
  color: #004d40;
}

.category-count {
  font-size: 1rem;
  color: #666;
}

.content-message {
  padding: 20px;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
}
</style>
