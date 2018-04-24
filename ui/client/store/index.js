import createLogger from 'vuex/dist/logger'
import createPersistedState from 'vuex-persistedstate'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  token: null,
  username: null,
  loggedIn: false
}

const mutations = {
  LOGIN (state, { token, username }) {
    state.token = token
    state.loggedIn = true
    state.username = username
  },
  LOGOUT (state) {
    state.token = null
    state.username = null
    state.loggedIn = false
  }
}

const actions = {
  authenticate ({ commit }, data) {
    commit('LOGIN', data)
  },
  logout ({ commit }) {
    commit('LOGOUT')
  }
}

const store = new Vuex.Store({
  state,
  mutations,
  actions,
  plugins: [
    createLogger(),
    createPersistedState()
  ]
})

export default store
