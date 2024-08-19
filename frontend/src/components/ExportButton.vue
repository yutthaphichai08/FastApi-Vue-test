<template>
  <button @click="exportCSV" class="btn btn-primary">Export CSV</button>
</template>

<script>
export default {
  methods: {
    async exportCSV() {
      try {
        const response = await fetch("http://localhost:8000/admin/export");
        if (!response.ok) throw new Error("Failed to fetch CSV");
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "users.csv");
        document.body.appendChild(link);
        link.click();
        link.parentNode.removeChild(link);
      } catch (error) {
        console.error("Error exporting CSV:", error);
      }
    },
  },
};
</script>

<style scoped></style>
