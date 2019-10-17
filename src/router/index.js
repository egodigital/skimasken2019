import Vue from "vue"
import VueRouter from "vue-router"

import Login from "@/views/Login"
import Error404 from "@/views/404"
Vue.use(VueRouter);


export default new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/",
      name: 'login',
      component: Login,
      meta: {
        title: 'Login',
        requiresAuth: false
      }
    },
    {
      path: "/profile",
      name: "profile",
      component: () => import(/* webpackChunkName: "profile" */ '@/views/Profile.vue'),
      meta: {
        title: 'Profile',
        requiresAuth: true
      }
    },

    { path: "*", component: Error404 }
  ]
});
