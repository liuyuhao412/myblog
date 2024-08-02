<template>
    <div class="about-layout">
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
            <el-main>
                <div class="content">
                    <h2>关于我</h2>
                    <p>你好！我是一名热爱编程和技术的博客作者。在这里，我会分享我的技术文章、编程经验以及一些个人的生活感悟。</p>
                    <p>希望我的博客能够对你有所帮助。如果你对我发布的内容有任何问题或者建议，欢迎通过评论或者邮件联系我！</p>
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

const store = useStore();
const router = useRouter();

const activeIndex = ref<string>('/about');
const isLogIn: Ref<boolean> = computed(() => store.getters.isLogin);

const menuSelect = (index: string) => {
    activeIndex.value = index;
    router.push(index).catch(err => console.error(err));
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
.about-layout {
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
