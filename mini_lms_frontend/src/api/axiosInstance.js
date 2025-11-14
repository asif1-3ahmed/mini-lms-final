import axios from "axios";
const base = import.meta.env.VITE_API_BASE || "http://localhost:8000/api";
const instance = axios.create({ baseURL: base });

instance.interceptors.request.use(config => {
  const user = JSON.parse(localStorage.getItem("user"));
  if (user?.token) config.headers.Authorization = `Bearer ${user.token}`;
  return config;
});

export default instance;
