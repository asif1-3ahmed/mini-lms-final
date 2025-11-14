import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import { Link } from "react-router-dom";

export default function CourseList() {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
        axios.get("courses/").then((res) => setCourses(res.data.results || res.data)).catch(console.error);
    }, []);

    return (
        <div className="p-6">
            <div className="flex justify-between items-center mb-4">
                <h1 className="text-xl font-bold">Courses</h1>
                <Link
                    to="/courses/new"
                    className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
                >
                    Add Course
                </Link>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {courses.map((c) => (
                    <div key={c.id} className="border p-4 rounded shadow hover:shadow-lg">
                        <h3 className="font-semibold text-lg">{c.title}</h3>
                        <p className="text-sm text-gray-600">{c.description}</p>
                        <Link to={`/courses/${c.id}`} className="text-blue-600 hover:underline">
                            View
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
}
