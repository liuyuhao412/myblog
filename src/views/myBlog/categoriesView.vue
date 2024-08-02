<template>
    <div class="categories-layout">
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
                        <h3>{{ userInfo.username }}</h3>
                        <img :src="userInfo.avatar" alt="头像" class="profile-avatar" />
                        <p>{{ userInfo.email }}</p>
                        <p>{{ userInfo.info }}</p>
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
                    <div class="categories-grid">
                        <el-card v-for="category in categories" :key="category.id" class="category-card">
                            <h3 class="card-title">{{ category.name }}</h3>
                            <p class="card-description">{{ category.description }}</p>
                            <el-button type="text" @click="viewCategory(category.id)">查看文章</el-button>
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
import { computed, ref, Ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { UserInfo, CategoryItem } from '@/types';

const store = useStore();
const router = useRouter();

const activeIndex = ref<string>('/categories');
const isLogIn: Ref<boolean> = computed(() => store.getters.isLogin);

const tags = [
    '标签一', '标签二', '标签三', '标签四', '标签五',
    '标签六', '标签七', '标签八', '标签九', '标签十',
    '标签11', '标签12', '标签13', '标签14', '标签15',
];

const userInfo = ref<UserInfo>({
    username: '用户名',
    avatar: 'https://via.placeholder.com/100',
    email: 'user@example.com',
    info: '这是一段个人简介。',
});

const categories = ref<CategoryItem[]>([
    { id: 1, name: '技术', description: '关于技术的文章' },
    { id: 2, name: '生活', description: '关于生活的文章' },
    { id: 3, name: '学习', description: '关于学习的文章' },
    { id: 4, name: '旅行', description: '关于旅行的文章' },
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

const viewCategory = (categoryId: number) => {
    router.push(`/category/${categoryId}`);
}
</script>

<style scoped>
.categories-layout {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
}

.header {
    background: linear-gradient(90deg, #4169E1, #1E90FF);
    color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    border-radius: 8px 8px 0 0;
}

.header h1 {
    font-size: 2rem;
    font-weight: bold;
    margin: 0;
    transition: color 0.3s;
}

.header h1:hover {
    color: #dfe6ff;
}

.menu {
    flex-grow: 1;
    margin-left: 40px;
    font-size: 1.5rem;
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
}

.main-container {
    display: flex;
    margin-top: 20px;
}

.sidebar {
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile h3,
.tags h3 {
    font-size: 1.5rem;
    color: #333;
    margin-bottom: 10px;
}

.profile p {
    font-size: 1rem;
    color: #666;
    line-height: 1.6;
}

.profile {
    text-align: center;
}

.profile-avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 10px;
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
    transition: background-color 0.3s;
    border-radius: 4px;
}

.tag-item:hover {
    background-color: #d0d0d0;
    color: #000;
}


.categories-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.category-card {
    flex: 1 1 calc(50% - 20px);
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.category-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.card-title {
    font-size: 1.5rem;
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
}

.footer {
    text-align: center;
    padding: 10px;
    background: linear-gradient(90deg, #1E90FF, #4169E1);
    color: #fff;
    margin-top: 20px;
    border-radius: 0 0 8px 8px;
    font-size: 1rem;
}

.footer p {
    margin: 0;
}
</style>
