import React, { useEffect, useState } from "react";
import api from "../../api/axios";
import { Link } from "react-router-dom";

export default function StudentCourses() {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        api.get("/api/courses/")
            .then((res) => setCourses(res.data.results || res.data))
            .catch(console.error);
    }, []);

    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold mb-6">Available Courses</h1>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {courses.map((course) => (
                    <div
                        key={course.id}
                        className="border p-4 rounded-xl bg-white shadow hover:shadow-lg transition"
                    >
                        <h2 className="text-xl font-semibold">{course.title}</h2>

                        <p className="text-gray-600 text-sm mt-2">
                            {course.description?.slice(0, 80) || "No description available."}
                        </p>

                        {/* FIXED: correct variable → course.id */}
                        <Link
                            to={`/courses/${course.id}/info`}
                            className="inline-block mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
                        >
                            View Course
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
}
