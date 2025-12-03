import React, { useEffect, useState } from "react";
import api from "../api/axios";
import { Link } from "react-router-dom";

export default function StudentQuizList() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    loadCourses();
  }, []);

  const loadCourses = async () => {
    try {
      const res = await api.get("/api/courses/");
      setCourses(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Available Quizzes</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {courses.map((c) => (
          <Link key={c.id} to={`/student/quiz/${c.id}`} className="block">
            <div className="p-4 bg-blue-100 hover:bg-blue-200 rounded-lg shadow">
              <h2 className="text-xl font-semibold">{c.title}</h2>
              <p className="text-gray-600 text-sm mt-2">
                {c.description?.slice(0, 60)}...
              </p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
