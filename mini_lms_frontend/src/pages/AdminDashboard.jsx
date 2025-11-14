import React, { useEffect, useState } from "react";
import axios from "../api/axiosInstance";
import { Link } from "react-router-dom";

export default function AdminDashboard() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    axios.get("/courses/").then((res) => setCourses(res.data));
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Admin Dashboard</h1>

      <Link
        to="/admin/create-course"
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        + Create Course
      </Link>

      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
        {courses.map((c) => (
          <div key={c.id} className="p-4 bg-white shadow rounded">
            <h2 className="font-bold text-xl">{c.title}</h2>
            <p>{c.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
