import App from "@/App.vue"
import Vue from "vue"
import router from "@/router"
import store from '@/store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false;

// Axios
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
