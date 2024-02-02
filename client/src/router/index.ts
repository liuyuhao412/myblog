import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path:'/',
    redirect:'/index'
  },
  {
    path: '/index',
    name: 'Index',
    component: () => import('@/views/blog/Index_view.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
