<template>
  <div class="category" v-for="category in categories" :key="category.id">
    <div class="form-check">
      <input
        class="form-check-input"
        type="checkbox"
        :value="category"
        :id="category.id"
        v-model="category.checked"
      />
      <label class="form-check-label" for="flexCheckDefault">
        {{ category.name }}
      </label>
    </div>
  </div>
  <button type="button" class="btn btn-primary category-button" @click="search">
    Search
  </button>

  <div class="container">
    <div class="row row-cols-3">
      <div class="col" v-for="product in products" :key="product._id">
        <div class="card product">
          <router-link
            :to="{ path: '/product/' + product.id }"
            style="text-decoration: none; color: inherit"
          >
            <img :src="product.photo" class="card-img-top" alt="..." />
            <div class="card-body">
              <h5 class="card-title">{{ product.title }}</h5>
              <p class="card-text">{{ product.description }}</p>
              <p class="card-text">Price: {{ product.price }}</p>
              <p class="card-text">Stock: {{ product.stock }}</p>
            </div>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      basket: [],
      products: [],
      categories: [],
    };
  },

  created() {
    this.getProducts();
    this.getProductCategories();
  },

  methods: {
    search() {
      let category_string = "";

      let categories = this.categories.filter((category) => {
        return category.checked;
      });
      let category_ids = categories.map((category) => {
        return category.id;
      });

      for (let i = 0; i < category_ids.length; i++) {
        category_string = category_string + "," + category_ids[i];
      }

      category_string = category_string.substring(1);

      if (category_string == "") {
        this.getProducts();
        return;
      }

      axios
        .get("http://127.0.0.1:8000/api/products/", {
          params: { category: category_string },
        })
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },

    getProducts() {
      axios
        .get("http://127.0.0.1:8000/api/products/")
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getProductCategories() {
      axios
        .get("http://127.0.0.1:8000/api/product-categories/")
        .then((response) => {
          this.categories = response.data;
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
.product {
  margin: 10px;
}

.product:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  font-size: 25px;
  color: yellowgreen;
}

.col {
  padding: 10px;
  max-width: 30%;
}

.category {
  margin-left: 50px;
}

.category-button {
  margin-left: 50px;
}
</style>
