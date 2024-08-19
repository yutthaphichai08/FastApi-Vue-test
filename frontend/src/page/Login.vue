<template>
  <div class="container">
    <div class="form-container">
      <h1>เข้าสู่ระบบ</h1>
      <form @submit.prevent="handleSubmit" class="form-content">
        <div class="form-group">
          <label for="email">Email:</label>
          <input
            type="text"
            v-model="formData.email"
            id="email"
            required
            class="form-input"
          />
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input
            type="password"
            v-model="formData.password"
            id="lastName"
            required
            class="form-input"
          />
        </div>

        <button type="submit" class="form-button">ส่งข้อมูล</button>
      </form>
    </div>
  </div>
  <button class="btn btn-primary floating-button" @click="handleButtonClick">
    Back
  </button>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      formData: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    async handleSubmit() {
      try {
        const apiUrl = "http://localhost:8000/login";
        axios
          .post(apiUrl, this.formData)
          .then(async (response) => {
            // console.log("res", response);
            const data = response.data;
            // console.log("jwt", data.jwt);
            if (data.jwt) {
              localStorage.setItem("session", data.jwt);
              window.location.href = "/application";
              alert("เข้าสู่ระบบสำเร็จ");
            } else {
              console.log("เกิดข้อผิดพลาดกรุณาลองใหม่");
            }
          })
          .catch((err) => {
            if (err.response) {
              const statusCode = err.response.status;
              if (statusCode === 401) {
                alert("รหัสผ่านหรือชื่อผู้ใช้ไม่ถูกต้อง");
              } else {
                alert("เกิดข้อผิดพลาดในการเข้าสู่ระบบ");
              }
            } else if (err.request) {
              alert("ไม่สามารถเชื่อมต่อกับเซิร์ฟเวอร์ได้");
            } else {
              alert("เกิดข้อผิดพลาดในการส่งคำขอ");
            }
            // console.error("Error details:", err);
          });

        this.formData = {
          email: "",
          password: "",
        };
      } catch (error) {
        console.error("Error :", error);
        alert("เกิดข้อผิดพลาด");
      }
    },
    handleButtonClick() {
      window.location.href = "/";
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
  z-index: 1050;
}
</style>
