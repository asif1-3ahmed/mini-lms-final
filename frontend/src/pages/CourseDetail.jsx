import React, { useEffect, useState, useContext } from "react";
import axios from "../api/axios";
import { useParams, useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

export default function CourseDetail() {
  const { user } = useContext(AuthContext);
  const { id } = useParams();
  const nav = useNavigate();

  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchCourse = async () => {
      try {
        const res = await axios.get(`/api/courses/${id}/`);
        setCourse(res.data);
      } catch (err) {
        console.error(err.response?.data || err.message);
        setError("Failed to load course information ❌");
      } finally {
        setLoading(false);
      }
    };
    fetchCourse();
  }, [id]);

  if (loading) return <p className="text-center mt-10 text-lg font-semibold">Loading course details...</p>;
  if (error) return <p className="text-center mt-10 text-red-500 text-lg font-semibold">{error}</p>;
  if (!course) return null;

  return (
    <div className="min-h-screen bg-[#fff6f4] p-6">
      <div className="max-w-6xl mx-auto">

        <h1 className="text-4xl font-extrabold text-center text-[#c84b31] mb-2">
          {course.title}
        </h1>

        <p className="text-center text-gray-700 mb-6 text-lg max-w-3xl mx-auto">
          {course.overview || course.description}
        </p>

        {/* COURSE INFO GRID */}
        <div className="bg-white rounded-2xl shadow-lg p-6 grid md:grid-cols-2 gap-6 mb-6">
          <div>
            <h2 className="text-2xl font-bold text-[#c84b31] mb-3">📘 Overview</h2>
            <p className="text-gray-800 leading-relaxed">{course.overview}</p>

            <h2 className="text-2xl font-bold text-[#c84b31] mt-4 mb-3">⏳ Duration</h2>
            <p className="text-gray-700 font-medium">{course.duration}</p>

            <h2 className="text-2xl font-bold text-[#c84b31] mt-4 mb-3">🧠 Skills You’ll Learn</h2>
            <div className="flex flex-wrap gap-2">
              {course.skills.map((s, i) => (
                <span key={i} className="px-3 py-1 bg-[#ffe7df] text-[#c84b31] text-sm rounded-full border border-[#c84b31]">
                  {s}
                </span>
              ))}
            </div>
          </div>

          <div>
            <h2 className="text-2xl font-bold text-[#c84b31] mb-3">📑 Modules</h2>
            <ul className="list-disc list-inside text-gray-800 space-y-2">
              {course.modules.map((m, i) => (
                <li key={i}>{m}</li>
              ))}
            </ul>

            <h2 className="text-2xl font-bold text-[#c84b31] mt-4 mb-3">🚀 Career Paths</h2>
            <ul className="list-disc list-inside text-gray-800 space-y-2">
              {course.career_paths.map((c, i) => (
                <li key={i}>{c}</li>
              ))}
            </ul>
          </div>
        </div>

        {/* ROADMAP */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
          <h2 className="text-3xl font-bold text-[#c84b31] mb-4">🗺 Learning Roadmap</h2>
          <div className="space-y-4">
            {course.roadmap.map((r, i) => (
              <div key={i} className="p-4 rounded-xl border border-[#c84b31] bg-[#fff0ec]">
                <h3 className="text-xl font-bold text-[#c84b31]">Step {i + 1}</h3>
                <p className="text-gray-800">{r}</p>
              </div>
            ))}
          </div>
        </div>

        {/* FAQ */}
        <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
          <h2 className="text-3xl font-bold text-[#c84b31] mb-4">❓ Frequently Asked Questions</h2>
          <div className="space-y-3">
            {course.faq.map((f, i) => (
              <div key={i} className="p-4 rounded-xl bg-[#panel-ac] border-l-4 border-[#c84b31]">
                <p className="font-bold text-[#c84b31]">{f.question}</p>
                <p className="text-gray-900">{f.answer}</p>
              </div>
            ))}
          </div>
        </div>

        {/* VIDEOS SECTION */}
        {course.videos?.length > 0 && (
          <div className="bg-white rounded-2xl shadow-lg p-6">
            <h2 className="text-3xl font-bold text-[#c84b31] mb-4">🎥 Course Videos</h2>
            <div className="grid md:grid-cols-2 gap-4">
              {course.videos.map((v, i) => (
                <div
                  key={i}
                  className="border rounded-xl p-3 hover:bg-[#ffe7df] cursor-pointer transition"
                  onClick={() => nav(`/courses/${id}`)}
                >
                  <h3 className="text-lg font-bold text-[#c84b31]">{v.title}</h3>
                  <p className="text-gray-700 text-sm">{v.description}</p>
                  <p className="text-xs text-gray-600 mt-1">Duration: {v.duration}</p>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* EDIT OPTIONS ONLY FOR ADMIN */}
        {user?.role === "admin" && (
          <div className="flex justify-center gap-4 mt-6">
            <button onClick={() => nav(`/courses/${id}/edit`)} className="px-5 py-2 bg-[#c84b31] text-white rounded-full font-bold shadow-md">
              ✏ Edit Course
            </button>
            <button className="px-5 py-2 bg-red-600 text-white rounded-full font-bold shadow-md">
              🗑 Delete Course
            </button>
          </div>
        )}

      </div>
    </div>
  );
}
