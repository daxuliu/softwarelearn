import Vue from 'vue'
import VueRouter from 'vue-router'
import loginForm from '../views/loginForm.vue'
import Home from '../views/Home.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'login',
    component: loginForm
  },
  {
      path: '/reg',
      name: 'reg',
      component: () => import('../views/regForm.vue')
  },
  {
    path: '/home',
    name: 'home',
    component: Home,
    children: [
      {
        path: 'list',
        name: 'list',
        component: () => import( '../views/List.vue')
      },
      {
        path: 'user',
        name: 'user',
        component: () => import('../views/User.vue')
      },
      {
        path: 'edit',
        name: 'edit',
        component: () => import('../views/Edit.vue')
      },
    ]
  },
  {
    path: '/add',
    name: 'add',
    component: () => import('../views/Add.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  linkActiveClass: 'active',
  routes
})

export default router
