<template>
  <div class="home">
    <div class="text-center">
      <h2 class="font-bold text-2xl">Welcome to Shopping Care</h2>

      <p>The best jacket store online</p>
    </div>

    <div>
      <div class="bg-green-700">
        <h2 class="font-bold text-xl text-center mt-10">OUR LATEST PRODUCT</h2>
      </div>

      <div :key="product.id" v-for="product in latestProducts">
        <div class="box">
          <div>
            <img :src="product.get_thumbnail" alt="" />
          </div>
          <h3>{{ product.name }}</h3>
          <p>${{ product.price }}</p>
          View Details
        </div>
      </div>
    </div>

    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  </div>
</template>

<script>
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    HelloWorld,
  },
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    getLatestProducts() {
      axios
        .get("/api/v1/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
