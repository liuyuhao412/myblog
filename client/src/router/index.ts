import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/index'
  },
  {
    path: '/index',
    name: 'Index',
    component: () => import('@/views/blog/Index_view.vue'),
    children: [
      {
        path: '/index',
        redirect: '/home'
      },
      {
        path: "/home",
        name: "home",
        component: () => import('@/views/blog/index_home.vue'),
      },
      {
        path: "/community",
        name: "community",
        component: () => import('@/views/blog/index_community.vue'),
      },
      {
        path: "/my_info",
        name: "my_info",
        component: () => import('@/views/blog/index_my_info.vue'),
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
