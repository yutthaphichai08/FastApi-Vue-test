import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
// import './style.css'

// createApp(App).mount("#app");

const app = createApp(App);
app.use(router);
app.mount("#app");
