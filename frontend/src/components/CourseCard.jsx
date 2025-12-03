import React from "react";
import { Link } from "react-router-dom";

export default function CourseCard({ course }) {
    return (
        <div className="border p-4 rounded shadow bg-white">
            <h3 className="text-xl font-semibold">{course.title}</h3>
            <p className="text-gray-600">{course.description}</p>

            <div className="mt-3 flex gap-4">
                <Link
                    to={`/courses/${course.id}`}
                    className="text-blue-600 hover:underline"
                >
                    View
                </Link>

                <Link
                    to={`/courses/edit/${course.id}`}
                    className="text-green-600 hover:underline"
                >
                    Edit
                </Link>
            </div>
        </div>
    );
}
