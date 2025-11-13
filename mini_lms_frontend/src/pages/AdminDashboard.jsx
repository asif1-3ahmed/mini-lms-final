import React, { useEffect, useState } from "react";
import API from "../api/axiosInstance";
import { Link } from "react-router-dom";

export default function AdminDashboard(){
  const [courses,setCourses] = useState([]);
  useEffect(()=>{ API.get("/courses/").then(r=>setCourses(r.data)).catch(()=>{}); }, []);
  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-2xl font-bold">Admin Dashboard</h1>
        <Link to="/admin/new" className="p-2 bg-green-600 text-white rounded">Create Course</Link>
      </div>
      <div className="space-y-3">
        {courses.map(c=>(
          <div key={c.id} className="bg-white p-3 rounded shadow flex justify-between">
            <div>
              <h3 className="font-semibold">{c.title}</h3>
              <p className="text-sm">{c.description?.slice(0,100)}</p>
            </div>
            <div className="flex items-center gap-2">
              <Link to={`/admin/edit/${c.id}`} className="p-2 bg-yellow-400 rounded">Edit</Link>
              <button onClick={async ()=>{ await API.delete(`/courses/${c.id}/`); setCourses(cs=>cs.filter(x=>x.id!==c.id)); }} className="p-2 bg-red-500 text-white rounded">Delete</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
