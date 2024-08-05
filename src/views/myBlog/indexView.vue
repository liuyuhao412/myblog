<template>
    <div class="blog-layout">
        <Header />
        <el-container class="main-container">
            <Sidebar />
            <el-main>
                <div class="content">
                    <!-- 登录状态显示用户内容 -->
                    <div v-if="isLogin" class="content-grid">
                        <el-card v-for="item in contentItems" :key="item.id" class="content-card"
                            @click="navigateToDetail(item.id)">
                            <h3 class="card-title">{{ item.title }}</h3>
                            <p class="card-description">{{ item.description }}</p>
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
import Header from '@/components/myBlog/headerView.vue';
import Sidebar from '@/components/myBlog/siderView.vue';
import Footer from '@/components/myBlog/footerView.vue';
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { ContentItem } from '@/types';

const store = useStore();
const router = useRouter();

const isLogin = computed(() => store.getters.isLogin);

const contentItems = ref<ContentItem[]>([
    { id: 1, title: '文章标题一', description: '这是文章一的简要描述。' },
    { id: 2, title: '文章标题二', description: '这是文章二的简要描述。' },
    { id: 3, title: '文章标题三', description: '这是文章三的简要描述。' },
    { id: 4, title: '文章标题4', description: '这是文章4的简要描述。' },
]);

const navigateToDetail = (id: number) => {
    router.push({ name: 'ArticleDetail', params: { id } });
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
    gap: 20px;
}

.content-card {
    flex: 1 1 calc(50% - 40px);
    padding: 15px;
    background-color: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
    cursor: pointer;
}

.content-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.card-title {
    font-size: 1.6rem;
    margin-bottom: 10px;
}

.card-description {
    font-size: 1rem;
    color: #666;
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