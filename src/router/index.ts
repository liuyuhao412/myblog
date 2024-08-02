import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/index'
  },
  {
    path: '/index',
    name: 'index',
    component: () => import('@/views/myBlog/indexView.vue')
  },
  {
    path: '/categories',
    name: 'categories',
    component: () => import('@/views/myBlog/categoriesView.vue')
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/myBlog/aboutMeView.vue')
  },
  {
    path: '/login_view',
    name: 'login_view',
    component: () => import('@/views/myBlog/base/loginView.vue')
  },
  {
    path: '/register_view',
    name: 'register_view',
    component: () => import('@/views/myBlog/base/registerView.vue')
  },
  {
    path: '/:catchAll(.*)',
    name: '404',
    component: () => import('@/views/page404View.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
