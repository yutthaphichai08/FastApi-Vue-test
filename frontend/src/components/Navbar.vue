<template>
  <nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark">
    <div class="container-fluid">
      <!-- <a class="navbar-brand" href="/users" style="color: white">Login</a> -->

      <div class="container-button">
        <button
          type="button"
          class="btn btn-success"
          data-bs-toggle="modal"
          data-bs-target="#exampleModalCreate"
        >
          New
        </button>
        <ExportButton />
        <ImportButton />
      </div>
      <button type="button" class="btn btn-danger" @click="clearLocalStorage">
        <i class="bi bi-power"></i>
      </button>
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
    clearLocalStorage() {
      const userConfirmed = window.confirm("คุณต้องการออกจากระบบใช่หรือไม่?");
      if (userConfirmed) {
        try {
          localStorage.clear();
          window.location.href = "/login";
        } catch (error) {
          console.error("Failed to logout", error);
        }
      }
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
