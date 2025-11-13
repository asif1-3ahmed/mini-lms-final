import React, { useEffect, useState } from "react";
import API from "../api/axiosInstance";
import { Link } from "react-router-dom";

export default function CourseList(){
  const [courses,setCourses]=useState([]);
  useEffect(()=>{ API.get("/courses/").then(r=>setCourses(r.data)).catch(()=>{}); },[]);
  return (
    <div>
      <h2 className="text-2xl mb-4">Courses</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {courses.map(c=>(
          <div key={c.id} className="bg-white p-4 rounded shadow">
            <h3 className="text-xl font-semibold">{c.title}</h3>
            <p className="text-sm">{c.description?.slice(0,140)}</p>
            <Link to={`/courses/${c.id}`} className="text-blue-600 inline-block mt-2">View course</Link>
          </div>
        ))}
      </div>
    </div>
  );
}
