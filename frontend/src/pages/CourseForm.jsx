import React, { useState, useEffect } from "react";
import axios from "../api/axios";
import { useNavigate, useParams } from "react-router-dom";

export default function CourseForm() {
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");
  const nav = useNavigate();
  const { id } = useParams(); // <-- If ID exists, we are editing

  // -----------------------------
  // LOAD EXISTING COURSE DATA
  // -----------------------------
  useEffect(() => {
    if (id) {
      axios
        .get(`courses/${id}/`)
        .then((res) => {
          setTitle(res.data.title);
          setDesc(res.data.description);
        })
        .catch(() => alert("Failed to load course"));
    }
  }, [id]);

  // -----------------------------
  // FORM SUBMIT HANDLER
  // -----------------------------
  const submit = async (e) => {
    e.preventDefault();

    try {
      if (id) {
        // EDIT MODE
        await axios.put(`courses/${id}/`, {
          title,
          description: desc,
        });
        alert("Course updated successfully!");
      } else {
        // CREATE MODE
        await axios.post("courses/", {
          title,
          description: desc,
        });
        alert("Course created successfully!");
      }

      nav("/manage-courses");
    } catch (err) {
      alert("Failed to save course");
      console.error(err);
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-3">
        {id ? "Edit Course" : "Create New Course"}
      </h2>

      <form onSubmit={submit} className="space-y-4">
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Course Title"
          className="w-full p-2 border rounded"
          required
        />

        <textarea
          value={desc}
          onChange={(e) => setDesc(e.target.value)}
          placeholder="Course Description"
          className="w-full p-2 border rounded"
          rows="4"
        />

        <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          {id ? "Update Course" : "Create Course"}
        </button>
      </form>
    </div>
  );
}
