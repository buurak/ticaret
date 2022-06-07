<template>
  <div id="app">
    <Navbar />
    <router-view></router-view>
  </div>
  <br /><br /><br /><br /><br /><br />
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style>
</style>
