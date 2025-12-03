// src/pages/student/StudentCourses.jsx
import React, { useEffect, useState } from "react";
import api from "../../api/axios";
import { useNavigate } from "react-router-dom";

export default function StudentCourses() {
    const [courses, setCourses] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        api.get("/api/courses/")
            .then((res) => setCourses(res.data.results || res.data))
            .catch(console.error);
    }, []);

    return (
        <div className="p-6">
            <h1 className="text-2xl font-bold mb-4">Available Courses</h1>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {courses.map(course => (
                    <div
                        key={course.id}
                        className="p-6 bg-white shadow rounded-lg border cursor-pointer hover:shadow-lg"
                        onClick={() => navigate(`/student/course/${course.id}`)}
                    >
                        <h2 className="text-xl font-semibold">{course.title}</h2>
                        <p className="text-gray-600 mt-2">{course.category}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
