import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import { useNavigate } from "react-router-dom";
import { Search, Edit2, Trash2, PlusCircle, FileDown } from "lucide-react";

export default function ManageCourses() {
  const [courses, setCourses] = useState([]);
  const [filtered, setFiltered] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");
  const nav = useNavigate();

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const res = await axios.get("/api/courses/");
        setCourses(res.data);
        setFiltered(res.data);
      } catch (err) {
        console.error(err);
        setError("Failed to load courses ❌");
      } finally {
        setLoading(false);
      }
    };
    fetchCourses();
  }, []);

  useEffect(() => {
    setFiltered(
      courses.filter((c) =>
        c.title.toLowerCase().includes(search.toLowerCase())
      )
    );
  }, [search, courses]);

  const deleteCourse = async (id) => {
    if (!window.confirm("Are you sure you want to delete this course?")) return;
    try {
      await axios.delete(`/api/courses/${id}/`);
      setCourses(courses.filter((c) => c.id !== id));
      alert("✅ Course deleted!");
    } catch (err) {
      console.error(err);
      alert("❌ Failed to delete course");
    }
  };

  const exportCSV = () => {
    const csv = filtered
      .map(c => `${c.id},"${c.title}","${c.description}"`)
      .join("\n");
    const blob = new Blob([`ID,Title,Description\n${csv}`], {
      type: "text/csv",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "courses.csv";
    a.click();
    URL.revokeObjectURL(url);
  };

  if (loading)
    return <p className="text-center mt-20 text-xl text-gray-500">Loading Courses… ⏳</p>;

  if (error)
    return <p className="text-center mt-20 text-xl text-red-500 font-semibold">{error}</p>;

  return (
    <div className="min-h-screen bg-white px-6 py-8">
      <div className="max-w-7xl mx-auto">

        {/* Header */}
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-4xl font-bold text-gray-900">👑 Manage Courses</h1>
          <button
            onClick={() => nav("/courses/new")}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-xl shadow hover:bg-blue-700 transition text-sm font-medium"
          >
            <PlusCircle size={16} /> Add Course
          </button>
        </div>

        {/* Filter Bar */}
        <div className="flex flex-wrap items-center gap-4 mb-8">
          {/* Search */}
          <div className="relative flex items-center w-full sm:w-72">
            <Search size={18} className="absolute left-3 text-gray-400" />
            <input
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search by title..."
              className="pl-10 py-2 w-full border border-gray-200 rounded-xl shadow-sm text-sm focus:ring-2 focus:ring-blue-500 outline-none"
            />
          </div>

          {/* Export CSV */}
          <button
            onClick={exportCSV}
            className="flex items-center gap-2 px-4 py-2 bg-indigo-600 text-white rounded-xl shadow hover:bg-indigo-700 transition text-sm font-medium"
          >
            <FileDown size={16} /> Export CSV
          </button>
        </div>

        {/* Courses Grid */}
        <div className="grid sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {filtered.map((course) => (
            <div
              key={course.id}
              onClick={() => nav(`/courses/${course.id}/info`)} // ✅ OPEN WEBSITE PAGE
                

              className="bg-white border border-gray-100 rounded-2xl shadow-md hover:shadow-lg transition p-4 cursor-pointer"
            >
              <h2 className="text-lg font-semibold text-gray-900 truncate mb-2">
                {course.title}
              </h2>

              <p className="text-gray-500 text-xs line-clamp-3 mb-4 h-12 overflow-hidden">
                {course.description}
              </p>

              {/* Actions */}
              <div
                className="flex items-center justify-between"
                onClick={(e) => e.stopPropagation()} // ❗ prevent opening website when clicking buttons
              >
                <button
                  onClick={() => nav(`/courses/${course.id}/edit`)}
                  className="flex items-center gap-1 text-blue-600 text-xs font-medium hover:underline"
                >
                  <Edit2 size={14} /> Edit
                </button>

                <button
                  onClick={() => deleteCourse(course.id)}
                  className="flex items-center gap-1 text-red-600 text-xs font-medium hover:underline"
                >
                  <Trash2 size={14} /> Delete
                </button>
              </div>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}
