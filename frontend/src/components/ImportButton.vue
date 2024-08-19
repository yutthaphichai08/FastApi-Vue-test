<template>
  <div>
    <input
      type="file"
      ref="fileInput"
      @change="handleFileUpload"
      style="display: none"
    />
    <button @click="triggerFileInput" class="btn btn-secondary">
      Import CSV
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    async handleFileUpload(event) {
      const file = event.target.files[0];
      if (!file) return;

      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch("http://localhost:8000/admin/import", {
          method: "POST",
          body: formData,
        });

        if (!response.ok) throw new Error("Failed to import CSV");
        location.reload();
        alert("CSV Imported Successfully");
      } catch (error) {
        console.error("Error importing CSV:", error);
        alert("Error importing CSV");
      }
    },
  },
};
</script>

<style scoped></style>
