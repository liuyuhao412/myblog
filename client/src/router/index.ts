import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/index'
  },
  {
    path: '/index',
    name: 'Index',
    component: () => import('@/views/blog/index_view.vue'),
    children: [
      {
        path: '/index',
        redirect: '/index_home'
      },
      {
        path: "/index_home",
        name: "index_home",
        component: () => import('@/views/blog/index_home.vue'),
      },
      {
        path: "/index_novel",
        name: "index_novel",
        component: () => import('@/views/blog/index_novel.vue'),
      },
      {
        path: "/index_music",
        name: "index_music",
        component: () => import('@/views/blog/index_music.vue'),
      },
      {
        path: "/index_class",
        name: "index_class",
        component: () => import('@/views/blog/index_class.vue'),
      },
      {
        path: "/index_my_info",
        name: "index_my_info",
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
