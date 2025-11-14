import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import { useParams, Link } from "react-router-dom";
import VideoPlayer from "./VideoPlayer";

export default function CourseDetail() {
  const { id } = useParams();
  const [course, setCourse] = useState(null);

  useEffect(() => {
    axios.get(`courses/${id}/`).then(res => setCourse(res.data)).catch(console.error);
  }, [id]);

  if (!course) return <div className="p-6">Loading...</div>;

  return (
    <div className="container mx-auto p-6">
      <Link to="/courses" className="text-blue-600 mb-4">← Back to Courses</Link>
      <h2 className="text-2xl font-bold mt-4 mb-2">{course.title}</h2>
      <p className="text-gray-600 mb-4">{course.description}</p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {course.videos.map(v => (
          <div key={v.id} className="bg-white p-4 rounded shadow">
            <h3 className="font-semibold mb-2">{v.title}</h3>
            <VideoPlayer url={v.storage_url} />
          </div>
        ))}
      </div>
    </div>
  );
}
