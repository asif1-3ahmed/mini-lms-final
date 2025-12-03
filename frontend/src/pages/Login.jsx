import React, { useState, useContext } from "react";
import axios from "../api/axios";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { setUser, login } = useContext(AuthContext);
  const nav = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    try {
      // ✅ Correct login endpoint
      const res = await axios.post("/api/auth/token/", { username, password });

      const token = {
        access: res.data.access,
        refresh: res.data.refresh,
      };

      login(token);  // ✅ save JWT

      // ✅ Fetch profile using correct backend URL
     const me = await axios.get("/api/auth/me/", {  // ✅ correct URL
  headers: { Authorization: `Bearer ${res.data.access}` }
});


      setUser(me.data); // ✅ Save user in context
      localStorage.setItem("access", res.data.access); // ✅ Store token for interceptor

      // ✅ Role based redirect
      if (me.data.role === "admin") {
        nav("/admin/manage-courses");
      } else {
        nav("/student");
      }

    } catch (err) {
      alert("Login failed ❌");
      console.error(err.response?.data || err.message);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form
        className="w-full max-w-md bg-white p-6 rounded shadow"
        onSubmit={submit}
      >
        <h2 className="text-2xl font-bold mb-4">Login</h2>

        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Username"
          className="w-full mb-3 p-2 border rounded"
          required
        />

        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          type="password"
          placeholder="Password"
          className="w-full mb-3 p-2 border rounded"
          required
        />

        <button
          className="w-full p-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
        >
          Login
        </button>
      </form>
    </div>
  );
}
