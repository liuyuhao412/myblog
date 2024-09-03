<template>
  <div class="blog-layout">
    <Header />
    <el-container class="main-container">
      <Sidebar />
      <el-main>
        <div class="content">
          <!-- 登录状态显示用户内容 -->
          <div v-if="isLogin" class="content-grid">
            <el-card v-for="item in contentItems" :key="item.id" class="content-card">
              <h3 class="card-title">{{ item.title }}</h3>
              <el-button
                class="delete-btn"
                type="primary"
                @click="navigateToDetail(item.id)"
                >详情查看</el-button
              >
              <el-button class="delete-btn" type="danger" @click="deleteArticle(item.id)"
                >删除</el-button
              >
            </el-card>
          </div>
          <!-- 未登录状态显示提示信息 -->
          <div v-else class="content-message">
            <p>请登录以查看内容。</p>
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
import { ref, computed, onMounted } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { getArticles, delArticle } from "@/api/article";

const store = useStore();
const router = useRouter();

const isLogin = computed(() => store.getters.isLogin);

const contentItems = ref();

const get_articles = async () => {
  const response = await getArticles();
  if (response.status == 200) {
    contentItems.value = response.data.data;
  }
};

const deleteArticle = async (id: number) => {
  const response = await delArticle(id);
  if (response.status == 200) {
    get_articles();
  }
};

onMounted(async () => {
  get_articles();
});
const navigateToDetail = (id: number) => {
  router.push({ name: "ArticleDetail", params: { id } });
};
</script>
<style scoped>
.blog-layout {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  border-radius: 15px;
}

.main-container {
  display: flex;
  margin-top: 20px;
  gap: 20px;
}

.content-grid {
  display: flex;
  flex-wrap: wrap;
}

.content-card {
  flex: 1 1 calc(50% - 40px);
  min-width: 450px; /* 调整卡片的最小宽度 */
  margin-bottom: 20px; /* 调整底部间距 */
  padding: 20px; /* 增加内部填充 */
  background-color: #fff;
  border-radius: 16px; /* 使卡片更加圆滑 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* 增加更大的阴影效果 */
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.content-card:hover {
  transform: translateY(-8px); /* 鼠标悬停时，增加明显的浮动效果 */
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15); /* 增加阴影效果 */
}

.card-title {
  font-size: 1.8rem; /* 增大标题字体 */
  font-weight: bold; /* 增加字体的权重 */
  margin-bottom: 15px;
  color: #333; /* 深色文字提高可读性 */
}
.detail-btn {
  margin-top: 10px;
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

.content-message {
  padding: 20px;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
}
</style>
