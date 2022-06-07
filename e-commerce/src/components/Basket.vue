<template>
  <section class="h-100 h-custom" style="background-color: #eee">
    <div class="container py-5 h-100">
      <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col">
          <div class="card">
            <div class="card-body p-4">
              <div class="row">
                <div class="col-lg-7">
                  <h5 class="mb-3">
                    <router-link to="/" class="text-body"
                      ><i class="fas fa-long-arrow-alt-left me-2"></i>Continue
                      shopping</router-link
                    >
                  </h5>
                  <hr />

                  <div
                    class="
                      d-flex
                      justify-content-between
                      align-items-center
                      mb-4
                    "
                  >
                    <div>
                      <p class="mb-1">Shopping cart</p>
                      <p class="mb-0">Your items cart</p>
                    </div>
                  </div>

                  <div
                    class="card mb-3 mb-lg-0"
                    v-for="item in basket.basket_items"
                    :key="item.id"
                  >
                    <div class="card-body">
                      <div class="d-flex justify-content-between">
                        <div class="d-flex flex-row align-items-center">
                          <div>
                            <img
                              :src="item.product.photo"
                              class="img-fluid rounded-3"
                              alt="Shopping item"
                              style="width: 65px"
                            />
                          </div>
                          <div class="ms-3">
                            <h5>{{ item.product.title }}</h5>
                          </div>
                        </div>

                        <div class="d-flex flex-row align-items-center">
                          <div style="width: 50px">
                            <h5 class="fw-normal mb-0">{{ item.quantity }}</h5>
                          </div>
                          <div style="width: 80px">
                            <h5 class="mb-0">${{ item.product.price }}</h5>
                          </div>
                          <a href="#!" style="color: #cecece"
                            ><i class="fas fa-trash-alt"></i
                          ></a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="col-lg-5">
                  <div class="card bg-primary text-white rounded-3">
                    <div class="card-body">
                      <div
                        class="
                          d-flex
                          justify-content-between
                          align-items-center
                          mb-4
                        "
                      >
                        <h5 class="mb-0">Card details</h5>
                      </div>

                      <form class="mt-4">
                        <div class="form-outline form-white mb-4">
                          <input
                            type="text"
                            id="typeName"
                            class="form-control form-control-lg"
                            siez="17"
                            placeholder="Cardholder's Name"
                          />
                          <label class="form-label" for="typeName"
                            >Cardholder's Name</label
                          >
                        </div>

                        <div class="form-outline form-white mb-4">
                          <input
                            type="number"
                            id="typeText"
                            class="form-control form-control-lg"
                            siez="17"
                            placeholder="1234 5678 9012 3457"
                            minlength="16"
                            maxlength="16"
                          />
                          <label class="form-label" for="typeText"
                            >Card Number</label
                          >
                        </div>

                        <div class="row mb-4">
                          <div class="col-md-6">
                            <div class="form-outline form-white">
                              <input
                                type="text"
                                id="typeExp"
                                class="form-control form-control-lg"
                                placeholder="MM/YYYY"
                                size="7"
                                minlength="7"
                                maxlength="7"
                              />
                              <label class="form-label" for="typeExp"
                                >Expiration</label
                              >
                            </div>
                          </div>
                          <div class="col-md-6">
                            <div class="form-outline form-white">
                              <input
                                type="password"
                                id="typeText"
                                class="form-control form-control-lg"
                                placeholder="&#9679;&#9679;&#9679;"
                                size="1"
                                minlength="3"
                                maxlength="3"
                              />
                              <label class="form-label" for="typeText"
                                >Cvv</label
                              >
                            </div>
                          </div>
                        </div>
                      </form>

                      <hr class="my-4" />

                      <button
                        type="button"
                        class="btn btn-info btn-block btn-lg"
                        @click="checkout()"
                      >
                        <div class="d-flex justify-content-between">
                          <span
                            >Checkout ${{ total }}
                            <i class="fas fa-long-arrow-alt-right ms-2"></i
                          ></span>
                        </div>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "Basket",

  data() {
    return {
      total: 0,
      basket: {},
    };
  },

  created() {
    this.getBasket();
  },

  methods: {
    getBasket() {
      axios
        .get("/api/basket/", {
          params: {
            user_id: localStorage.getItem("user_id"),
          },
        })
        .then((response) => {
          this.basket = response.data;
          for (let i = 0; i < this.basket.basket_items.length; i++) {
            this.total +=
              this.basket.basket_items[i].product.price *
              this.basket.basket_items[i].quantity;
          }
        });
    },

    checkout() {
      axios
        .post("/api/order/", {
          user_id: localStorage.getItem("user_id"),
        })
        .then(() => {
          alert("Checkout Complete");
          this.$router.push("/");
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
