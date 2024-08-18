<template>
  <button @click="exportCSV" class="btn btn-primary">Export CSV</button>
</template>

<script>
export default {
  methods: {
    async exportCSV() {
      try {
        const response = await fetch("http://127.0.0.1:8000/users/export");
        if (!response.ok) throw new Error("Failed to fetch CSV");
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "export.csv");
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
