import App from "@/App.vue"
import Vue from "vue"
import router from "@/router"
import store from '@/store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false;

/**
 * Axios
 */
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.axios.interceptors.response.use(response => response, error => {
  // Failed due to authentication (session timed out)
  if(error.response && error.response.status === 401 && store.getters['isLoggedIn']) {
    store.dispatch('logout')
    router.replace({ name: 'login' })

    return Promise.resolve()
  }

  return Promise.reject(error)
});

/**
 * Router
 */
router.beforeEach((to, from, next) => {
  // Set page title
  document.title = to.meta.title

  const requiresAuth = to.meta.requiresAuth

  // Check if user is logged in
  if (requiresAuth && !store.getters['isLoggedIn']) {
      next({ name: 'login' })
      return
  } else if(requiresAuth === false && store.getters['isLoggedIn']) {
      // Redirect to profile page if logged in
      next({ name: 'profile' })
      return
  }

  next()
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App),
  created() {
    // Check if user still has a session
    try {
      this.$http.get('/api/user/me')
      .then(() => {
        if(this.$route.name === 'login')
          this.$router.push({ name: 'profile' })
      }).catch(err => {
        console.log(err)
      })
    } catch(e) {
      console.log(e)
    }
  }
}).$mount("#app");
