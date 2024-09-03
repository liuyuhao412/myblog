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

          <el-button class="update-btn" type="primary" @click="updateArticle"
            >修改</el-button
          >
          <el-button class="update-btn" type="default" @click="goBack">返回</el-button>
        </div>
      </el-main>
    </el-container>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from "@/components/myBlog/headerView.vue";
import Footer from "@/components/myBlog/footerView.vue";
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { getArticle } from "@/api/article";

const route = useRoute();
const router = useRouter();
const articleId = parseInt(route.params.id as string, 10);

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
  font-size: 1.2rem;
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
  font-size: 1rem;
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
