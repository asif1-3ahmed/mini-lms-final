import React, { useState, useEffect } from "react";
import axios from "../api/axiosInstance";
import { useNavigate, useParams } from "react-router-dom";

export default function CourseForm() {
  const navigate = useNavigate();
  const { id } = useParams();   
  const isEdit = Boolean(id);

  const [form, setForm] = useState({
    title: "",
    description: "",
    category: "",
  });

  const [videos, setVideos] = useState([]);          // uploaded videos list
  const [newVideos, setNewVideos] = useState([]);    // new files before upload
  const [loading, setLoading] = useState(false);

  // Load course data + existing videos
  useEffect(() => {
    if (isEdit) {
      axios.get(`/courses/${id}/`).then((res) => {
        setForm({
          title: res.data.title,
          description: res.data.description,
          category: res.data.category,
        });
      });

      // load existing videos
      axios.get(`/videos/course/${id}/`)
        .then((res) => setVideos(res.data))
        .catch((err) => console.log(err));
    }
  }, [isEdit, id]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Upload new videos
  const uploadVideos = async (courseId) => {
    if (newVideos.length === 0) return;

    const uploadPromises = newVideos.map((file) => {
      const formData = new FormData();
      formData.append("course", courseId);
      formData.append("video", file);

      return axios.post("/videos/", formData, {
        headers: { "Content-Type": "multipart/form-data" }
      });
    });

    await Promise.all(uploadPromises);
  };

  // Delete video
  const handleDeleteVideo = async (videoId) => {
    await axios.delete(`/videos/${videoId}/`);
    setVideos(videos.filter((v) => v.id !== videoId));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      let course;

      if (isEdit) {
        const res = await axios.put(`/courses/${id}/`, form);
        course = res.data;
      } else {
        const res = await axios.post("/courses/", form);
        course = res.data;
      }

      // Upload new videos
      await uploadVideos(course.id);

      navigate("/courses");
    } catch (error) {
      console.error("Error saving course:", error);
    }

    setLoading(false);
  };

  return (
    <div className="max-w-3xl mx-auto bg-white p-6 shadow rounded">

      <h1 className="text-3xl font-bold mb-6">
        {isEdit ? "Edit Course" : "Create Course"}
      </h1>

      <form onSubmit={handleSubmit} className="space-y-6">

        {/* Title */}
        <div>
          <label className="block font-semibold mb-1">Title</label>
          <input
            className="w-full border p-2 rounded"
            name="title"
            value={form.title}
            onChange={handleChange}
            required
          />
        </div>

        {/* Category */}
        <div>
          <label className="block font-semibold mb-1">Category</label>
          <input
            className="w-full border p-2 rounded"
            name="category"
            value={form.category}
            onChange={handleChange}
          />
        </div>

        {/* Description */}
        <div>
          <label className="block font-semibold mb-1">Description</label>
          <textarea
            className="w-full border p-2 rounded h-32"
            name="description"
            value={form.description}
            onChange={handleChange}
          />
        </div>

        {/* Video upload */}
        <div>
          <label className="block font-semibold mb-1">Upload Videos</label>
          <input
            type="file"
            accept="video/*"
            multiple
            onChange={(e) => setNewVideos([...e.target.files])}
            className="block w-full border p-2 rounded"
          />

          {newVideos.length > 0 && (
            <p className="text-sm text-blue-600 mt-1">
              {newVideos.length} new video(s) selected
            </p>
          )}
        </div>

        {/* Existing videos */}
        {isEdit && videos.length > 0 && (
          <div className="mt-4">
            <h3 className="text-xl font-semibold mb-2">Existing Videos</h3>
            <ul className="space-y-2">
              {videos.map((v) => (
                <li
                  key={v.id}
                  className="flex justify-between items-center p-2 border rounded"
                >
                  <span>{v.title || "Video"}</span>
                  <button
                    type="button"
                    onClick={() => handleDeleteVideo(v.id)}
                    className="text-red-600 hover:underline"
                  >
                    Delete
                  </button>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Submit */}
        <button
          disabled={loading}
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
        >
          {loading ? "Saving..." : isEdit ? "Update Course" : "Create Course"}
        </button>

      </form>
    </div>
  );
}
