import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Main from '@/components/mainPage/index'
import Index from '@/components/index/index'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/test',
      name: 'Test',
      component: Home
    },
    {
      path: '/main',
      name: 'main',
      component: Main
    },
  ]
})
