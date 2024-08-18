import { createRouter, createWebHistory } from "vue-router";
import Home from "../page/Home.vue";
import ListUsers from "../page/ListUsers.vue";
import Login from "../page/Login.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/application",
      name: "ListUsers",
      component: ListUsers,
    },
  ],
});

export default router;
