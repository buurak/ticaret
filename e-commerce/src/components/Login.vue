<template>
  <div class="container">
    <form>
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          v-model="email"
        />
        <div id="emailHelp" class="form-text">
          We'll never share your email with anyone else.
        </div>
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input
          type="password"
          class="form-control"
          id="exampleInputPassword1"
          v-model="password"
        />
      </div>

      <button type="button" class="btn btn-primary" @click="login()">
        Submit
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      email: "",
      password: "",
    };
  },

  methods: {
    login() {
      axios
        .post("/api/login/", {
          email: this.email,
          password: this.password,
        })
        .then((response) => {
          localStorage.setItem("email", response.data.email);
          localStorage.setItem("user_id", response.data.id);
          this.$router.push("/");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
form {
  max-width: 400px;
  margin: 0 auto;
  margin-top: 10%;
}
</style>
