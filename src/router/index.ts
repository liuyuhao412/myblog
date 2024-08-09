import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import { ElMessage } from 'element-plus';
import { useStore } from 'vuex';


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/index',
    meta: { requiresAuth: true }
  },
  {
    path: '/index',
    name: 'index',
    component: () => import('@/views/myBlog/indexView.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/categories',
    name: 'categories',
    component: () => import('@/views/myBlog/categoriesView.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/myBlog/aboutMeView.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/login_view',
    name: 'login_view',
    component: () => import('@/views/myBlog/base/loginView.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/register_view',
    name: 'register_view',
    component: () => import('@/views/myBlog/base/registerView.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/article/:id',
    name: 'ArticleDetail',
    component: () => import('@/views/myBlog/function/articleDetail.vue'),
    meta: { requiresAuth: true },
    props: true
  },
  {
    path: '/article/edit/:id?',
    name: 'ArticleEdit',
    component: () => import('@/views/myBlog/function/articleEdit.vue'),
    meta: { requiresAuth: true },
    props: true
  },
  {
    path: '/:catchAll(.*)',
    name: '404',
    component: () => import('@/views/page404View.vue'),
    meta: { requiresAuth: false }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach(async (to, from, next) => {
  const store = useStore();
  const isLogin = store.getters.isLogin;
  const requiresAuth = to.meta.requiresAuth;

  if (requiresAuth) {
      if (!isLogin) {
          next('/login_view');
          return;
      }
      try {
          // 验证 Token 是否有效
          await store.dispatch('checkAuth');
          if (store.getters.isLogin) {
              next();
          } else {
              ElMessage.error('Token 无效或已过期，请重新登录');
              localStorage.removeItem('token');
              store.dispatch('logout'); 
              next('/login_view');
          }
      } catch (error) {
          ElMessage.error('验证失败，请稍后再试');
          localStorage.removeItem('token');
          store.dispatch('logout'); 
          next('/login_view');
      }
  } else {
      next();
  }
});


export default router
