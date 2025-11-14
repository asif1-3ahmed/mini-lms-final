import React, { useEffect, useState, useContext } from "react";
import axios from "../api/axios";
import { Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

export default function CourseList() {
    const [courses, setCourses] = useState([]);
    const { user } = useContext(AuthContext);

    useEffect(() => {
        axios.get("/courses/").then((res) => setCourses(res.data.results || res.data)).catch(console.error);
    }, []);

    return (
        <div className="p-6">
            <div className="flex justify-between items-center mb-4">
                <h1 className="text-xl font-bold">Courses</h1>
                {user?.role === "admin" && (
                    <Link
                        to="/courses/new"
                        className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
                    >
                        Add Course
                    </Link>
                )}
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {courses.map((c) => (
                    <div key={c.id} className="bg-white border p-4 rounded shadow hover:shadow-lg transition">
                        <h3 className="font-semibold text-lg">{c.title}</h3>
                        <p className="text-sm text-gray-600 mb-2">{c.description}</p>
                        {c.category && <p className="text-xs text-gray-500 mb-3">Category: {c.category}</p>}
                        <Link to={`/courses/${c.id}`} className="text-blue-600 hover:underline">
                            View Details
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
}
