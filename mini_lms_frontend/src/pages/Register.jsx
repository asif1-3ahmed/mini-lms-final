import React, { useState } from "react";
import axios from "../api/axiosInstance";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const nav = useNavigate();
  const [form, setForm] = useState({
    full_name: "",
    email: "",
    password: "",
  });

  const submit = async (e) => {
    e.preventDefault();
    await axios.post("/users/register/", form);
    nav("/login");
  };

  return (
    <div className="flex justify-center items-center min-h-screen">
      <form
        onSubmit={submit}
        className="bg-white p-6 shadow rounded w-96 space-y-4"
      >
        <h1 className="text-2xl font-bold text-center">Register</h1>

        <input
          type="text"
          className="w-full border p-2 rounded"
          placeholder="Full Name"
          onChange={(e) => setForm({ ...form, full_name: e.target.value })}
        />

        <input
          type="email"
          className="w-full border p-2 rounded"
          placeholder="Email"
          onChange={(e) => setForm({ ...form, email: e.target.value })}
        />

        <input
          type="password"
          className="w-full border p-2 rounded"
          placeholder="Password"
          onChange={(e) => setForm({ ...form, password: e.target.value })}
        />

        <button className="bg-green-600 text-white py-2 rounded w-full">
          Register
        </button>
      </form>
    </div>
  );
}
