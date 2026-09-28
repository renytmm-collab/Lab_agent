import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path:'/',redirect:'/manager/home'},
    {path: '/manager',
      name:'Layout',
      component: () => import('@/layouts/Layout.vue'),
      children:[
        {path: 'home',name:'Home',component: () => import('@/views/Home.vue')},
        {path: 'lab',name:'Lab',component: () => import('@/views/Lab.vue')}
    ]},
    {path:'/login',name:'Login',component: () => import('@/views/Login.vue')},
    {path:'/register',name:'Register',component: () => import('@/views/Register.vue')}
  ] 
})

export default router
