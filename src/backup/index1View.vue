<template>
    <div class="blog-layout">
        <el-header class="header">
            <h1>myBlog</h1>
            <el-menu mode="horizontal" class="menu" :default-active="activeIndex" @select="menuSelect">
                <el-menu-item index="/">首页</el-menu-item>
                <el-menu-item index="/categories">分类</el-menu-item>
                <el-menu-item index="/about">关于我</el-menu-item>
            </el-menu>
            <el-input class="search-input" placeholder="请输入搜索内容" clearable></el-input>
            <el-button type="primary" @click="handleLogin">{{ isLogIn ? '退出' : '登录' }}</el-button>
        </el-header>

        <el-container class="main-container">
            <el-aside width="300px">
                <div class="sidebar">
                    <div class="profile">
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
                    </div>
                    <div class="tags">
                        <h3>标签云</h3>
                        <div class="tag-list">
                            <el-tag v-for="tag in tags" :key="tag" class="tag-item">
                                {{ tag }}
                            </el-tag>
                        </div>
                    </div>
                </div>
            </el-aside>

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

        <el-footer class="footer">
            <p>&copy; 2024 个人博客</p>
            <p>Github: liuyuhao412</p>
        </el-footer>
    </div>
</template>

<script setup lang="ts">
import { ref, computed, Ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { UserInfo, ContentItem } from '@/types';

const store = useStore();
const router = useRouter();


const activeIndex = ref<string>('/');
const isLogIn: Ref<boolean> = computed(() => store.getters.isLogin);

const tags = ref<string[]>([
    '标签一', '标签二', '标签三', '标签四', '标签五',
    '标签六', '标签七', '标签八', '标签九', '标签十',
    '标签11', '标签12', '标签13', '标签14', '标签15',
]);

const userInfo = ref<UserInfo>({
    username: '用户名',
    avatar: 'https://via.placeholder.com/100',
    email: 'user@example.com',
    info: '这是一段个人简介。',
    articleCount: 10,
    tagCount: 5,
});

const contentItems = ref<ContentItem[]>([
    { id: 1, title: '文章标题一', description: '这是文章一的简要描述。' },
    { id: 2, title: '文章标题二', description: '这是文章二的简要描述。' },
    { id: 3, title: '文章标题三', description: '这是文章三的简要描述。' },
    { id: 4, title: '文章标题4', description: '这是文章4的简要描述。' },
]);

const menuSelect = (index: string) => {
    activeIndex.value = index;
    router.push(index);
}

const handleLogin = () => {
    if (isLogIn.value) {
        store.dispatch('logout');
    } else {
        router.push('/login_view');
    }
}

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

.blog-layout:hover {
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.2);
}

.header {
    background: linear-gradient(90deg, #4169E1, #1E90FF);
    color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    border-radius: 12px 12px 0 0;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.header h1 {
    font-size: 2.2rem;
    font-weight: bold;
    margin: 0;
}

.header h1:hover {
    color: #dfe6ff;
}

.menu {
    flex-grow: 1;
    margin-left: 40px;
    font-size: 1.6rem;
}

.el-menu-item {
    transition: color 0.3s;
}

.el-menu-item:hover {
    color: #dfe6ff;
}

.search-input {
    max-width: 300px;
    margin: 0 2em;
    border-radius: 6px;
}

.search-input:focus {
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
}

.main-container {
    display: flex;
    margin-top: 20px;
    gap: 20px;
}

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


.profile-avatar:hover {
    transform: scale(1.1);
}


.profile-avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 10px;
    border: 3px solid #fff;
    transition: transform 0.3s;
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

.footer {
    text-align: center;
    padding: 10px;
    background: linear-gradient(90deg, #1E90FF, #4169E1);
    color: #fff;
    margin-top: 20px;
    border-radius: 0 0 12px 12px;
    font-size: 1rem;
}

.footer p {
    margin: 0;
}
</style>