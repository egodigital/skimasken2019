export default {
  state: {
    user: JSON.parse(localStorage.getItem('user')) || null
  },
  actions: {
    login({ commit }) {
      commit('authSuccess', { user: "test" })
    },
    logout({ commit }) {
      commit('authReset')
    }
  },
  mutations: {
    authSuccess(state, payload) {
      state.user = payload.user
    },
    authReset(state, payload) {
      state.user = payload.user
    }
  },
  getters: {
    isLoggedIn: state => state.user !== null
  },
}