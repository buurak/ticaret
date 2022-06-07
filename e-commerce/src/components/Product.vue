<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <div class="card">
          <img :src="product.photo" class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <p class="card-text">{{ product.description }}</p>
            <p class="card-text">Price: {{ product.price }}</p>
            <p class="card-text">Stock: {{ product.stock }}</p>
            <p class="card-text">Size: {{ product.size }}</p>

            <button class="btn btn-danger" @click="addToBasket(product.id)">
              Add To Basket
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Product",
  data() {
    return {
      id: this.$route.params.id,
      basket: [],
      product: {},
      email: localStorage.getItem("email"),
    };
  },

  created() {
    this.getProduct();
  },

  methods: {
    getProduct() {
      axios
        .get(`http://127.0.0.1:8000/api/product/${this.id}`)
        .then((response) => {
          this.product = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addToBasket(id) {
      axios
        .post("http://127.0.0.1:8000/api/basket/", {
          email: this.email,
          id: id,
          quantity: 1,
          user_id: localStorage.getItem("user_id"),
        })
        .then((response) => {
          this.basket = response.data;
          this.getBasket();
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.col {
  max-width: 70%;
}
</style>
