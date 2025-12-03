import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import { useNavigate } from "react-router-dom";
import { Search, FileDown } from "lucide-react";

export default function CourseList() {
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

  const exportCSV = () => {
    const csv = filtered
      .map(c => `"${c.id}","${c.title}","${c.description}"`)
      .join("\n");
    const blob = new Blob([`ID,Title,Description\n${csv}`], { type: "text/csv" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "courses.csv";
    a.click();
    URL.revokeObjectURL(url);
  };

  if (loading) return <p className="text-center mt-20 text-xl text-gray-500">Loading Courses… ⏳</p>;
  if (error) return <p className="text-center mt-20 text-xl text-red-500 font-semibold">{error}</p>;

  return (
    <div className="min-h-screen bg-white px-6 py-8">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold text-gray-900 mb-6">📘 Course Catalog</h1>

        {/* Filter bar */}
        <div className="flex flex-wrap items-center gap-4 mb-8">
          {/* Search */}
          <div className="relative flex items-center w-full sm:w-72">
            <Search size={18} className="absolute left-3 text-gray-400" />
            <input
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search by title..."
              className="pl-10 py-2 w-full border border-gray-200 rounded-xl shadow-sm text-sm focus:ring-2 focus:ring-indigo-500 outline-none"
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
              className="bg-white border border-gray-100 rounded-2xl shadow-md hover:shadow-xl transition p-4"
            >
              {/* Title */}
              <h2 className="text-lg font-semibold text-gray-900 line-clamp-2 mb-2">
                {course.title}
              </h2>

              {/* Description */}
              <p className="text-gray-500 text-xs line-clamp-4 mb-3">
                {course.description}
              </p>

              {/* Tags */}
              <div className="flex flex-wrap gap-2 mb-3">
                <span className="px-2 py-1 bg-blue-50 text-blue-600 text-[10px] font-medium rounded-lg">Tech</span>
                <span className="px-2 py-1 bg-green-50 text-green-600 text-[10px] font-medium rounded-lg">LMS</span>
                <span className="px-2 py-1 bg-purple-50 text-purple-600 text-[10px] font-medium rounded-lg">Project</span>
              </div>

              {/* View Details */}
              <button
                onClick={() => nav(`/courses/${course.id}/info`)}

                className="text-indigo-600 text-[11px] font-semibold hover:underline"
              >
                View Details →
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
