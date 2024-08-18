<script>
import axios from "axios";

export default {
  data() {
    return {
      formData: {
        firstname: "",
        lastname: "",
        address: "",
        salary: 0,
      },
    };
  },

  methods: {
    async handleSubmit() {
      try {
        const apiUrl = "http://127.0.0.1:8000/users";

        const response = await axios.post(apiUrl, this.formData);

        console.log("Response:", response.data);
        location.reload();
        alert("บันทึกข้อมูลสำเร็จ");
        this.formData = {
          firstname: "",
          lastname: "",
          address: "",
          salary: 0,
        };
      } catch (error) {
        console.error("Error submitting form:", error);
        alert("เกิดข้อผิดพลาดในการส่งข้อมูล");
      }
    },
  },
};
</script>

<template lang="">
  <!-- Modal -->
  <div
    class="modal fade"
    id="exampleModalCreate"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">กรอกข้อมูล</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="handleSubmit">
            <div class="">
              <label for="recipient-name" class="col-form-label"
                >Firstname:</label
              >
              <input
                type="text"
                class="form-control"
                id="firstname"
                required
                v-model="formData.firstname"
              />
            </div>
            <div class="">
              <label for="recipient-name" class="col-form-label"
                >Lastname:</label
              >
              <input
                type="text"
                class="form-control"
                id="lastname"
                required
                v-model="formData.lastname"
              />
            </div>
            <div class="">
              <label for="message-text" class="col-form-label">Address:</label>
              <textarea
                class="form-control"
                id="address"
                v-model="formData.address"
              ></textarea>
            </div>
            <div class="mb-3">
              <label for="recipient-name" class="col-form-label">Salary</label>
              <input
                type="number"
                class="form-control"
                id="salary"
                v-model="formData.salary"
              />
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button type="button" class="btn btn-primary" @click="handleSubmit">
            Save
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style></style>
