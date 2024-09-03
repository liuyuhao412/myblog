<template>
  <div class="article-detail">
    <Header />
    <el-container class="main-container">
      <el-main>
        <div class="content">
          <el-card class="article-card">
            <h1 class="article-title">{{ article.title }}</h1>
            <p class="article-meta">
              作者: {{ article.author }} | 时间: {{ article.date }}
            </p>
            <div class="article-content">
              <p>{{ article.content }}</p>
            </div>
          </el-card>

          <el-button class="update-btn" type="default" @click="updateArticle"
            >修改</el-button
          >
          <el-button class="update-btn" type="default" @click="goBack">返回</el-button>

          <!-- 评论部分 -->
          <div class="comments-section">
            <h3>评论</h3>
            <div v-if="comments.length">
              <div v-for="comment in comments" :key="comment.id" class="comment">
                <p class="comment-author">{{ comment.author }}</p>
                <p class="comment-content">{{ comment.content }}</p>
                <p>{{ comment.date }}</p>
              </div>
            </div>
            <p v-else>还没有评论，快来发表你的看法吧！</p>

            <!-- 登录状态下显示评论输入框 -->
            <div v-if="isLogin" class="comment-form">
              <el-input
                class="comment-input"
                v-model="newComment"
                placeholder="输入你的评论"
              ></el-input>
              <el-button class="comment-submit" type="primary" @click="submitComment"
                >提交评论</el-button
              >
            </div>
            <div v-else class="login-message">
              <p>请登录后发表评论。</p>
            </div>
          </div>
        </div>
      </el-main>
    </el-container>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from "@/components/myBlog/headerView.vue";
import Footer from "@/components/myBlog/footerView.vue";
import { ref, computed, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { getArticle } from "@/api/article";
import { useStore } from "vuex";

const route = useRoute();
const router = useRouter();
const store = useStore();
const articleId = parseInt(route.params.id as string, 10);

const isLogin = computed(() => store.getters.isLogin);

const article = ref({
  title: "",
  author: "",
  content: "",
  date: "",
});

const get_article = async () => {
  const response = await getArticle(articleId);
  if (response.status == 200) {
    article.value.title = response.data.data.title;
    article.value.author = response.data.data.name;
    article.value.content = response.data.data.content;
    article.value.date = response.data.data.date;
  } else {
    console.log("获取文章失败");
  }
};

onMounted(async () => {
  get_article();
});

const comments = ref([
  { id: 1, author: "用户1", content: "这是一条评论内容。", date: "2024-08-05 11:50" },
  { id: 2, author: "用户2", content: "这是另一条评论内容。", date: "2024-08-06 12:30" },
]);

const newComment = ref("");

onMounted(() => {
  // 根据 articleId 加载文章详情和评论
  // article.value = loadArticleDetails(articleId);
  // comments.value = loadComments(articleId);
});

const submitComment = () => {
  if (newComment.value.trim()) {
    comments.value.push({
      id: comments.value.length + 1,
      author: "当前用户", // 可以从 store 中获取当前用户
      content: newComment.value,
      date: new Date().toISOString().split("T")[0],
    });
    newComment.value = "";
  }
};
const goBack = () => {
  router.push({ name: "index" });
};

const updateArticle = () => {
  router.push({ name: "ArticleEdit", params: { id: articleId } });
};
</script>
<style scoped>
.article-detail {
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
}

.content {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.article-card {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 10px;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.article-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 10px;
  color: #333;
  text-align: center;
}

.article-meta {
  font-size: 0.8em;
  color: #6c757d;
  margin-bottom: 10px;
}

.article-content {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #333;
  text-align: left;
}

.update-btn {
  width: 100px;
  height: 40px;
  font-size: 18px;
}

.comments-section {
  text-align: left;
  margin-top: 10px;
}

.comments-section h3 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.comment {
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
  background-color: #f2f2f2;
}

.comments-title {
  margin-bottom: 15px;
  color: #333;
  font-size: 1.2rem;
  font-weight: bold;
}

.comment-author {
  font-weight: bold;
}

.comment-content {
  font-size: 1rem;
  line-height: 1.6;
}

.comment-form {
  margin-top: 10px;
  align-items: center;
}

.comment-input {
  width: 85%;
  height: 40px;
  font-size: 1rem;
}

.comment-submit {
  width: 10%;
  height: 40px;
  border: none;
  font-size: 0.9rem;
  cursor: pointer;
  margin-left: 10px;
}

.login-message {
  margin-top: 20px;
  color: #999;
}
</style>
