import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Register(){
  const { registerUser } = useAuth();
  const [form,setForm] = useState({username:"",email:"",password:"",confirm:""});
  const nav = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    if (form.password !== form.confirm) return alert("Passwords mismatch");
    const ok = await registerUser({username:form.username,email:form.email,password:form.password,role:"STUDENT"});
    if (ok) nav("/login"); else alert("Failed");
  };

  return (
    <div className="max-w-md mx-auto mt-24 bg-white p-6 rounded shadow">
      <h2 className="text-2xl mb-4">Register</h2>
      <form onSubmit={submit}>
        <input required value={form.username} onChange={e=>setForm({...form,username:e.target.value})} placeholder="Username" className="w-full p-2 border mb-3"/>
        <input required value={form.email} onChange={e=>setForm({...form,email:e.target.value})} placeholder="Email" className="w-full p-2 border mb-3"/>
        <input required type="password" value={form.password} onChange={e=>setForm({...form,password:e.target.value})} placeholder="Password" className="w-full p-2 border mb-3"/>
        <input required type="password" value={form.confirm} onChange={e=>setForm({...form,confirm:e.target.value})} placeholder="Confirm" className="w-full p-2 border mb-3"/>
        <button type="submit" className="w-full p-2 bg-green-600 text-white rounded">Create Account</button>
      </form>
    </div>
  );
}
