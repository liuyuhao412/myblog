<template>
    <div class="blog-layout">
        <Header />
        <el-container class="main-container">
            <Sidebar />
            <el-main>
                <div class="content">
                    <div class="content-grid">
                        <el-card v-for="item in contentItems" :key="item.id" class="content-card">
                            <h3 class="card-title">{{ item.title }}</h3>
                            <p class="card-description">{{ item.description }}</p>
                        </el-card>
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
import { ref } from 'vue';

import { ContentItem } from '@/types';

const contentItems = ref<ContentItem[]>([
    { id: 1, title: '文章标题一', description: '这是文章一的简要描述。' },
    { id: 2, title: '文章标题二', description: '这是文章二的简要描述。' },
    { id: 3, title: '文章标题三', description: '这是文章三的简要描述。' },
    { id: 4, title: '文章标题4', description: '这是文章4的简要描述。' },
]);

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
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    flex-grow: 1;
    margin-left: 10px;
    font-size: 1.1rem;
    line-height: 1.8;
}
</style>