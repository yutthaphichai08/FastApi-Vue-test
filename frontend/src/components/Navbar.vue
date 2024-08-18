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
      <div class="container-button">
        <ExportButton />
        <ImportButton />
      </div>
    </div>

    <ModalCreate ref="modal" />
  </nav>
</template>

<script>
import ModalCreate from "./ModalCreate.vue";
import ExportButton from "./ExportButton.vue";
import ImportButton from "./ImportButton.vue";

export default {
  components: {
    ModalCreate,
    ExportButton,
    ImportButton,
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
<style scoped>
.container-button {
  display: flex;
  gap: 6px;
}
</style>
