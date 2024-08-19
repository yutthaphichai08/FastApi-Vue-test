export default function auth() {
  if (!localStorage.getItem("session")) {
    alert("กรุณา Login");
    return "/login";
  }
}
