import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Login(){
  const { login } = useAuth();
  const [username,setUsername]=useState("");
  const [password,setPassword]=useState("");
  const nav = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    try {
      await login(username,password);
      const user = JSON.parse(localStorage.getItem("user"));
      if (user.role === "ADMIN") nav("/admin");
      else nav("/student");
    } catch {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="max-w-md mx-auto mt-24 bg-white p-6 rounded shadow">
      <h2 className="text-2xl mb-4">Login</h2>
      <form onSubmit={submit}>
        <input value={username} onChange={e=>setUsername(e.target.value)} placeholder="username" className="w-full p-2 border mb-3" />
        <input type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="password" className="w-full p-2 border mb-3" />
        <button className="w-full p-2 bg-blue-600 text-white rounded">Login</button>
      </form>
    </div>
  );
}
