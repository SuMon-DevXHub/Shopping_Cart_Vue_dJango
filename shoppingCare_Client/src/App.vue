<template>
  <div>
    <Navbar />

    <router-view class="h-[91vh]" />

    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/Header/Header.vue";
import Footer from "@/components/Footer/Footer.vue";
export default {
  components: { Navbar, Footer },
};
</script>

<style lang="scss">
</style>
