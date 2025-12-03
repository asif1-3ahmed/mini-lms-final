import React, { useEffect, useState } from "react";
import api from "../../api/axios";

export default function StudentProgress() {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    api.get("/api/courses/").then(res => {
      const all = res.data.results || res.data;
      loadProgress(all);
    });
  }, []);

  const loadProgress = async (courseList) => {
    const data = [];
    for (const c of courseList) {
      const res = await api.get(`/api/progress/${c.id}/`);
      const p = res.data;

      const totalModules = c.modules.length || 1;
      const completedModules = p.completed_modules.length;

      const percentage = Math.round((completedModules / totalModules) * 100);

      data.push({
        title: c.title,
        courseId: c.id,
        percentage,
        quiz: `${p.quiz_score}/${p.quiz_total}`
      });
    }
    setCourses(data);
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">My Progress</h1>

      {courses.map((c) => (
        <div key={c.courseId} className="p-4 bg-white rounded shadow mb-4">
          <h2 className="text-xl font-semibold">{c.title}</h2>

          <p className="mt-2">Course Progress: <b>{c.percentage}%</b></p>
          <p>Quiz Score: <b>{c.quiz}</b></p>

          <div className="w-full bg-gray-200 rounded h-3 mt-2">
            <div
              className="bg-blue-600 h-3 rounded"
              style={{ width: `${c.percentage}%` }}
            ></div>
          </div>
        </div>
      ))}
    </div>
  );
}
