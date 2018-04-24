import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { sync } from 'vuex-router-sync'
import App from './components/App'
import router from './router'
import store from './store'

Vue.use(VueAxios, axios)
sync(store, router)

const app = new Vue({
  router,
  store,
  ...App
})

export { app, router, store }
