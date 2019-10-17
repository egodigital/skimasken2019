import Vue from 'vue'

export default {
  state: {
    user: JSON.parse(localStorage.getItem('user')) || null
  },
  actions: {
    login({ commit }, userData) {
      return new Promise((resolve, reject) => {
        Vue.axios.post('/api/user/me/', userData)
        .then(resp => {
          commit('authSuccess', { user: resp.data })
          localStorage.setItem('user', JSON.stringify(resp.data))

          resolve(resp.user)
        })
        .catch(err => {
          commit('authReset')
          localStorage.removeItem('user')

          reject(err)
        })
      })
    },
    logout({ commit }) {
      Vue.axios.delete('/api/user/me/')
      .then(() => {
        commit('authReset')
        localStorage.removeItem('user')
      })
    }
  },
  mutations: {
    authSuccess(state, payload) {
      state.user = payload.user
    },
    authReset(state) {
      state.user = null
    }
  },
  getters: {
    isLoggedIn: state => state.user !== null
  },
}