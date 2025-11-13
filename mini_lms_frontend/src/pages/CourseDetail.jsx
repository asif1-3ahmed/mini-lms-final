import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import API from "../api/axiosInstance";
import VideoPlayer from "../components/VideoPlayer";

export default function CourseDetail(){
  const { id } = useParams();
  const [course,setCourse] = useState(null);
  useEffect(()=>{
    API.get(`/courses/${id}/`).then(r=>setCourse(r.data)).catch(()=>{});
  },[id]);
  if (!course) return <div>Loading...</div>;
  return (
    <div>
      <h1 className="text-3xl">{course.title}</h1>
      <p className="mb-4">{course.description}</p>
      <h2 className="text-2xl mt-6">Videos</h2>
      <div className="space-y-4">
        {course.videos?.map(v=>(
          <div key={v.id} className="bg-white p-3 rounded shadow">
            <h3 className="font-semibold">{v.title}</h3>
            <VideoPlayer url={v.video_file} />
          </div>
        ))}
      </div>
    </div>
  );
}
