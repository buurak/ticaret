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
        <label for="firstname" class="form-label">First Name</label>
        <input
          type="name"
          class="form-control"
          id="firstname"
          v-model="firstname"
        />
      </div>
      <div class="mb-3">
        <label for="lastname" class="form-label">Last Name</label>
        <input
          type="name"
          class="form-control"
          id="lastname"
          v-model="lastname"
        />
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
      <div class="mb-3">
        <label for="exampleInputPassword2" class="form-label"
          >Confirm Password</label
        >
        <input
          type="password"
          class="form-control"
          id="exampleInputPassword2"
          v-model="password_confirmation"
        />
      </div>

      <button type="button" class="btn btn-primary" @click="register()">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Register",
  data() {
    return {
      email: "",
      password: "",
      password_confirmation: "",
      firstname: "",
      lastname: "",
    };
  },

  methods: {
    register() {
      if (this.password !== this.password_confirmation) {
        alert("Passwords do not match");
        return;
      }

      axios
        .post("/api/register/", {
          email: this.email,
          password: this.password,
          first_name: this.firstname,
          last_name: this.lastname,
        })
        .then((response) => {
          console.log(response);
          this.$router.push("/login");
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
