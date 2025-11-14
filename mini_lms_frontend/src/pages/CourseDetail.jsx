import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "../api/axiosInstance";
import VideoPlayer from "../components/VideoPlayer";

export default function CourseDetail() {
  const { id } = useParams();
  const [course, setCourse] = useState(null);

  useEffect(() => {
    axios.get(`/courses/${id}/`).then((res) => setCourse(res.data));
  }, [id]);

  if (!course) return <p>Loading...</p>;

  return (
    <div>
      <h1 className="text-3xl font-bold mb-2">{course.title}</h1>
      <p className="mb-4">{course.description}</p>

      <h2 className="text-xl font-semibold mb-2">Videos</h2>

      <div className="space-y-4">
        {course.videos?.map((video) => (
          <div key={video.id} className="bg-white shadow p-4 rounded">
            <h3 className="text-lg font-bold">{video.title}</h3>
            <VideoPlayer url={video.video_url} />
          </div>
        ))}
      </div>
    </div>
  );
}
