<template>
  <div class="container">
    <div class="container">
      <div class="row row-cols-4">
        <div class="col" v-for="order in orders" :key="order.id">
          <div
            v-for="basket_item in order.basket_items"
            :key="basket_item.id"
          >
            <div class="card product">
              <img :src="basket_item.product.photo" class="card-img-top" alt="..." />
              <div class="card-body">
                <h5 class="card-title">{{ basket_item.product.title }}</h5>
                <p class="card-text">{{ basket_item.product.description }}</p>
                <p class="card-text">Price: {{ basket_item.product.price }}</p>
                <p class="card-text">Date: {{ basket_item.date_added.substring(0,10) }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "OrderHistory",
  data() {
    return {
      orders: [],
      email: localStorage.getItem("email"),
    };
  },

  created() {
    this.getOrderHistory();
  },

  methods: {
    getOrderHistory() {
      axios
        .get(`http://127.0.0.1:8000/api/order/`, {
          params: { user_id: localStorage.getItem("user_id") },
        })
        .then((response) => {
          this.orders = response.data;
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
.col {
  max-width: 70%;
}
</style>
