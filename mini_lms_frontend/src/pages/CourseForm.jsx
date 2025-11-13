import React, { useState, useEffect } from "react";
import API from "../api/axiosInstance";
import { useNavigate, useParams } from "react-router-dom";

export default function CourseForm(){
  const { id } = useParams();
  const [title,setTitle]=useState("");
  const [description,setDescription]=useState("");
  const nav = useNavigate();

  useEffect(()=>{
    if (id) API.get(`/courses/${id}/`).then(r=>{ setTitle(r.data.title); setDescription(r.data.description); });
  },[id]);

  const submit = async (e) => {
    e.preventDefault();
    if (id) await API.put(`/courses/${id}/`, { title, description });
    else await API.post("/courses/", { title, description, is_published: true});
    nav("/admin");
  };

  return (
    <div className="max-w-lg mx-auto bg-white p-6 rounded shadow">
      <h2 className="text-2xl mb-4">{id ? "Edit Course" : "Create Course"}</h2>
      <form onSubmit={submit}>
        <input value={title} onChange={e=>setTitle(e.target.value)} placeholder="Title" className="w-full p-2 border mb-3"/>
        <textarea value={description} onChange={e=>setDescription(e.target.value)} placeholder="Description" className="w-full p-2 border mb-3"></textarea>
        <button className="p-2 bg-blue-600 text-white rounded">{id ? "Update" : "Create"}</button>
      </form>
    </div>
  );
}
