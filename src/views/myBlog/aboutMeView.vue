<template>
  <div class="about-layout">
    <Header />

    <el-container class="main-container">
      <el-main>
        <div v-if="isLogin">
          <h2>关于我</h2>
          <p>
            你好！我是一名热爱编程和技术的博客作者。在这里，我会分享我的技术文章、编程经验以及一些个人的生活感悟。
          </p>
          <p>
            希望我的博客能够对你有所帮助。如果你对我发布的内容有任何问题或者建议，欢迎通过评论或者邮件联系我！
          </p>
        </div>
        <div v-else>
          <h2>关于我</h2>
          <p>你好！欢迎访问我的博客。如果你想查看更多内容，请登录。</p>
        </div>
      </el-main>
    </el-container>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from "@/components/myBlog/headerView.vue";
import Footer from "@/components/myBlog/footerView.vue";
import { computed } from "vue";
import { useStore } from "vuex";

const store = useStore();
const isLogin = computed(() => store.getters.isLogin);
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
</style>
