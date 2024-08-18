<script setup>
import NavbarVue from "../components/Navbar.vue";
import TableList from "../components/TableList.vue";
</script>

<template>
  <NavbarVue />
  <div class="container">
    <TableList />
  </div>
</template>

<style scoped>
.container {
  max-width: 1660px;
  margin-top: 16px;
}
</style>
