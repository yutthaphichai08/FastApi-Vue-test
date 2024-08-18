// const { createRouter, createWebHashHistory } = require("vue-router");

import { createRouter, createWebHistory } from "vue-router";
import Home from "../page/Home.vue";
import ListUsers from "../page/ListUsers.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
    {
      path: "/users",
      name: "ListUsers",
      component: ListUsers,
    },
  ],
});

export default router;
