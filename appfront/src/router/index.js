import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
// import Main from '@/components/mainPage/index'
import Index from '@/components/pages/index'
import Focus from '@/components/pages/focus'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',   // 主页
      name: 'index',
      component: Index
    },
    {
      path: '/focus',   //  降价通知商品页
      name: 'focus',
      component: Focus
    },
    {
      path: '/test',  // 测试页
      name: 'Test',
      component: Home
    },
    // {
    //   path: '/main',   // 原来丑丑的页，
    //   name: 'main',
    //   component: Main
    // },
  ]
})
