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
                    <div class="categories-list">
                        <div v-for="category in categories" :key="category.id" class="category-item">
                            <a class="category-name">{{ category.name }}</a>
                            <span class="category-count">({{ category.articleCount }})</span>
                        </div>
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
    articleCount: 10,
    tagCount: 5,
});

const categories = ref<CategoryItem[]>([
    { id: 1, name: '技术', articleCount: 10 },
    { id: 2, name: '生活', articleCount: 5 },
    { id: 3, name: '学习', articleCount: 8 },
    { id: 4, name: '旅行', articleCount: 3 },
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
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    border-radius: 10px;

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
    border-radius: 8px;
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
