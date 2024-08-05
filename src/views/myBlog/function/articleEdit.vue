<template>
  <div class="blog-layout" v-if="isLogIn">
    <Header />
    <el-container class="main-container">
      <el-main>
        <div class="article-form">
          <h2>{{ isEdit ? '编辑文章' : '写文章' }}</h2>
          <el-form :model="form" ref="form" label-width="50px">
            <el-form-item label="标题" prop="title" :rules="[{ required: true, message: '请输入标题', trigger: 'blur' }]">
              <el-input v-model="form.title"></el-input>
            </el-form-item>
            <el-form-item label="内容" prop="content" :rules="[{ required: true, message: '请输入内容', trigger: 'blur' }]">
              <el-input type="textarea" v-model="form.content" rows="10"></el-input>
            </el-form-item>
            <el-form-item class="form-footer">
              <el-button class="submit-btn" type="primary">{{ isEdit ? '更新' : '发布' }}</el-button>
              <el-button class="submit-btn" type="default" @click="handleCancel">返回</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-main>
    </el-container>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from '@/components/myBlog/headerView.vue';
import Footer from '@/components/myBlog/footerView.vue';
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const store = useStore();
const router = useRouter();
const isLogIn = computed(() => store.getters.isLogin);
const form = ref({
  title: '',
  content: ''
});

const articleId = route.params.id as string;
const isEdit = computed(() => !!articleId);

const handleCancel = () => {
  if (isEdit.value) {
    router.back(); // 返回上一页
  } else {
    router.push('/'); // 写文章时返回首页
  }
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

.article-form {
  padding: 20px;
}

.el-card {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-footer {
  gap: 10px;
}

.submit-btn {
  width: 100px;
  height: 40px;
  margin: 0 auto;
  font-size: 18px;
}
</style>