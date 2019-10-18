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
    {
      path: "/bookings",
      name: "bookings",
      component: () => import(/* webpackChunkName: "bookings" */ '@/views/Bookings.vue'),
      meta: {
        title: 'Bookings',
        requiresAuth: true
      }
    },
    {
      path: "/vehicles",
      name: "vehicles",
      component: () => import(/* webpackChunkName: "vehicles" */ '@/views/Vehicles.vue'),
      meta: {
        title: 'Vehicles',
        requiresAuth: true
      }
    },
    {
      path: "/blackboard",
      name: "blackboard",
      component: () => import(/* webpackChunkName: "blackboard" */ '@/views/Blackboard.vue'),
      meta: {
        title: 'Blackboard',
        requiresAuth: true
      }
    },
    {
      path: "/leaderboard",
      name: "leaderboard",
      component: () => import(/* webpackChunkName: "leaderboard" */ '@/views/Leaderboard.vue'),
      meta: {
        title: 'Leaderboard',
        requiresAuth: true
      }
    },

    { path: "*", component: Error404 }
  ]
});
