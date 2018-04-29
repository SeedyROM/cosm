import { shallow, createLocalVue } from '@vue/test-utils'
import VueRouter from 'vue-router'
import VueX from 'vuex'

const localVue = createLocalVue()
localVue.use(VueRouter)
const router = new VueRouter()

localVue.use(VueX)

export const mock = (component) => shallow(component, {
  localVue,
  router
})
