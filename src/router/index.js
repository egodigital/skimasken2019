import Vue from "vue"
import VueRouter from "vue-router"

import Login from "@/views/Login"
import Error404 from "@/views/404"
Vue.use(VueRouter);

// TODO Web Template Studio: Add routes for your new pages here.
export default new VueRouter({
  mode: "history",
  routes: [
    { path: "/", component: Login },

    { path: "*", component: Error404 }
  ]
});
