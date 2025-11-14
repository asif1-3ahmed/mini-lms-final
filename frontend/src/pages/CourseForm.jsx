import React, { useState } from "react";
import axios from "../api/axios";
import { useNavigate } from "react-router-dom";

export default function CourseForm() {
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");
  const nav = useNavigate();

  const submit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/courses/", {
        title,
        description: desc,
      });
      nav("/admin");
    } catch (err) {
      alert("Failed to create course");
      console.error(err);
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-lg font-bold mb-3">New Course</h2>
      <form onSubmit={submit} className="space-y-3">
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Title"
          className="w-full p-2 border rounded"
          required
        />
        <textarea
          value={desc}
          onChange={(e) => setDesc(e.target.value)}
          placeholder="Description"
          className="w-full p-2 border rounded"
        />
        <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          Create
        </button>
      </form>
    </div>
  );
}
