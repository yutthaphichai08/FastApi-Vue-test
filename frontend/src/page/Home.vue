<template>

  <div class="container">
  
    <div class="form-container">
      <h1>กรอกข้อมูลผู้สมัคร</h1>
      <form @submit.prevent="handleSubmit" class="form-content">
        <div class="form-group">
          <label for="firstName">ชื่อ:</label>
          <input
            type="text"
            v-model="formData.firstname"
            id="firstName"
            required
            class="form-input"
          />
        </div>
        <div class="form-group">
          <label for="lastName">นามสกุล:</label>
          <input
            type="text"
            v-model="formData.lastname"
            id="lastName"
            required
            class="form-input"
          />
        </div>
        <div class="form-group">
          <label for="address">ที่อยู่:</label>

          <textarea
            class="form-input"
            v-model="formData.address"
            id="address"
          ></textarea>
        </div>
        <div class="form-group">
          <label for="salary">เงินเดือนที่คาดหวัง:</label>
          <input
            type="number"
            v-model="formData.salary"
            id="salary"
            required
            class="form-input"
          />
        </div>
        <button type="submit" class="form-button">ส่งข้อมูล</button>
      </form>
    </div>
  </div>
  <button class="btn btn-primary floating-button" @click="handleButtonClick">Login</button>
</template>

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
        const apiUrl = "http://localhost:8000/application";

        const response = await axios.post(apiUrl, this.formData);

        console.log("Response:", response.data);
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
    handleButtonClick() {
      window.location.href = '/login'
    },
  },
};
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-content: center;
  padding-top: 50px;
}

.form-container {
  background-color: #fff;
  padding: 20px 40px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  box-sizing: border-box;
  transition: border-color 0.3s ease;
}

.form-input:focus {
  border-color: #007bff;
  outline: none;
}

.form-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 18px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.form-button:hover {
  background-color: #0056b3;
}
.floating-button {
  position: fixed;
  top: 1rem;
  right: 1rem;
  z-index: 1050; /* Ensure button is above other content */
}
</style>
