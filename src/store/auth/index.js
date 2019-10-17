export default {
  state: {
    user: JSON.parse(localStorage.getItem('user')) || null
  },
  actions: {
    login({ commit }) {
      const user = { name: 'test' }
      commit('authSuccess', { user })
      localStorage.setItem('user', JSON.stringify(user))
    },
    logout({ commit }) {
      commit('authReset')
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