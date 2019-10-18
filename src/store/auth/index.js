import Vue from 'vue'

export default {
  state: {
    user: JSON.parse(localStorage.getItem('user')) || null
  },
  actions: {
    login({ commit }, userData) {
      return new Promise((resolve, reject) => {
        Vue.axios.post('/api/user/me', userData)
        .then(resp => {
          const user = resp.data

          user.level = 3

          commit('authSuccess', { user: user })
          localStorage.setItem('user', JSON.stringify(user))

          resolve(user)
        })
        .catch(err => {
          commit('authReset')
          localStorage.removeItem('user')

          reject(err)
        })
      })
    },
    logout({ commit }) {
      return Vue.axios.delete('/api/user/me')
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