import Vue from 'vue'
import store from '../store'
import Router from 'vue-router'
import Home from '../views/Home'
import Profile from '../views/Profile'
import Login from '../views/Login'
import Logout from '../views/Logout'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/login',
      component: Login
    },
    {
      path: '/logout',
      component: Logout
    },
    {
      path: '/profile',
      component: Profile,
      secure: true
    }
  ]
})

router.beforeEach((to, from, next) => {
  router.options.routes.forEach((route) => {
    if (to.matched[0].path === route.path && route.secure) {
      if (store.state.loggedIn === false) {
        console.log('Not logged in! Redirecting...')
        return next({ path: '/login' })
      }
    }
  })
  next()
})

export default router
