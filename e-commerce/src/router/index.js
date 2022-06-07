import { createWebHistory, createRouter } from "vue-router";
import Home from "@/components/Home.vue";
import Product from "@/components/Product.vue";
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import Basket from "@/components/Basket.vue";


const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/product/:id",
    name: "Product",
    component: Product,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/basket",
    name: "Basket",
    component: Basket,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;