import React, { useEffect, useState } from "react";
import axios from "../api/axiosInstance";
import { Link } from "react-router-dom";

export default function CourseList() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    axios.get("/courses/").then((res) => setCourses(res.data));
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">Courses</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {courses.map((c) => (
          <Link
            key={c.id}
            to={`/courses/${c.id}`}
            className="p-4 bg-white shadow rounded"
          >
            <h2 className="text-xl font-bold">{c.title}</h2>
            <p>{c.description}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
