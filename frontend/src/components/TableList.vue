<script>
import axios from "axios";

export default {
  data() {
    return {
      tableData: [],
      user: {
        firstname: "",
        lastname: "",
        address: "",
        salary: 0,
      },
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      const jwt = await localStorage.getItem("session");
      // console.log('jwt--',jwt);

      const getData = async () => {
        try {
          const headers = new Headers();
          await headers.append(`authorization`,"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjQwODgyMTAsInN1YiI6MX0.UKYPZg6kNGg_kF9SezexPJ3k0aA-chWVwCtkNF29cdM")
          const response = await fetch(
            "http://localhost:8000/admin/application",
            {
              method: "GET",
              headers
            }
          );
          const data = await response.json();
          this.tableData = data
          // console.log(data);
        } catch (error) {
          console.log(error);
        }
      };
      getData();
    },
    async fetchUserData(userId) {
      try {
        const jwt = await localStorage.getItem("session");
        // console.log(jwt);
        const response = await axios.get(
          `http://localhost:8000/admin/application/${userId}`,
          {
            headers: {
              Authorization: jwt,
            },
          }
        );
        this.user = response.data;
      } catch (error) {
        window.location.href = "/login";
        console.error("Error fetching user data:", error);
      }
    },
    handleClick(userId) {
      // console.log(userId);
      this.fetchUserData(userId);
    },
    confirmDelete(userId) {
      if (confirm("Are you sure you want to delete this user?")) {
        this.deleteUser(userId);
        window.location.reload();
      }
    },
    async deleteUser(userId) {
      try {
        const jwt = await localStorage.getItem("session");
        const response = await axios.delete(
          `http://localhost:8000/admin/application/${userId}`,
          {
            headers: {
              Authorization: jwt,
            },
          }
        );
        this.user = response.data;
        console.log("User deleted successfully");
      } catch (error) {
        console.error("Error :", error);
      }
    },
    async handleSubmit(userId) {
      if (userId === null) {
        console.error("User ID is required for updating");
        return;
      }
      try {
        const jwt = await localStorage.getItem("session");
        await axios.put(
          `http://localhost:8000/admin/application/update/${userId}`,
          this.user,
          {
            headers: {
              Authorization: jwt,
            },
          }
        );
        console.log("User updated successfully");
        location.reload();
      } catch (error) {
        console.error("Error updating user data:", error);
      }
    },
    formatSalary(value) {
      if (value === null || value === undefined) return "";
      if (typeof value !== "number") return "";
      return value.toLocaleString();
    },
  },
};
</script>

<template lang="">
  <div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">First</th>
          <th scope="col">Last</th>
          <th scope="col">Address</th>
          <th scope="col">Salary</th>
          <th scope="col">Handle</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in tableData" :key="index">
          <th scope="row">{{ index + 1 }}</th>
          <td class="address-cell">{{ item.firstname }}</td>
          <td class="address-cell">{{ item.lastname }}</td>
          <td class="address-cell">{{ item.address }}</td>
          <td class="address-cell">{{ formatSalary(item.salary) }}</td>
          <td>
            <button
              type="button"
              class="btn btn-success"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              @click="handleClick(item.id)"
            >
              <i class="bi bi-pencil"></i>
              <!-- Bootstrap Icon for pencil -->
            </button>
            <button
              type="button"
              class="btn btn-danger ms-2"
              @click="confirmDelete(item.id)"
            >
              <i class="bi bi-trash"></i>
              <!-- Bootstrap Icon for trash -->
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <!-- Button trigger modal -->

  <!-- Modal -->
  <div
    class="modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Edit User</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form v-if="user" @submit.prevent="handleSubmit(user.id)">
            <div class="">
              <label for="recipient-name" class="col-form-label"
                >Firstname:</label
              >
              <input
                type="text"
                class="form-control"
                id="firstname"
                required
                v-model="user.firstname"
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
                v-model="user.lastname"
              />
            </div>
            <div class="">
              <label for="message-text" class="col-form-label">Address:</label>
              <textarea
                class="form-control"
                id="address"
                v-model="user.address"
              ></textarea>
            </div>
            <div class="mb-3">
              <label for="recipient-name" class="col-form-label">Salary</label>
              <input
                type="number"
                class="form-control"
                id="salary"
                v-model="user.salary"
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
          <button
            type="button"
            class="btn btn-primary"
            @click="handleSubmit(user.id)"
          >
            Update
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.address-cell {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 80px;
}
</style>
