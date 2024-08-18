<template>
  <nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark">
    <div class="container-fluid">
      <!-- <a class="navbar-brand" href="/users" style="color: white">Login</a> -->
      <button
        type="button"
        class="btn btn-success"
        data-bs-toggle="modal"
        data-bs-target="#exampleModalCreate"
      >
        New
      </button>
    </div>
    <ModalCreate ref="modal" />
  </nav>
</template>

<script>
import ModalCreate from "./ModalCreate.vue";

export default {
  components: {
    ModalCreate,
  },
  methods: {
    openModal() {
      const modalElement = this.$refs.modal.$el;
      const modal = new bootstrap.Modal(modalElement);
      modal.show();
    },
  },
};
</script>
<style scoped></style>
