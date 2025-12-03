import React from "react";
import { Link } from "react-router-dom";

export default function AdminDashboard() {
    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold mb-4">Admin Dashboard</h1>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">

                {/* Manage Courses */}
                <Link to="/admin/manage-courses" className="bg-blue-100 p-4 rounded cursor-pointer hover:bg-blue-200 text-gray-700 flex items-center justify-center">
                    Manage Courses
                </Link>

                {/* Upload Videos */}
                <Link to="/upload-video" className="bg-green-100 p-4 rounded cursor-pointer hover:bg-green-200 text-gray-700 flex items-center justify-center">
                    Upload Videos
                </Link>

                {/* Create Quiz */}
                <Link to="/admin/create-quiz" className="bg-purple-100 p-4 rounded cursor-pointer hover:bg-purple-200 text-gray-700 flex items-center justify-center">
                    Create Quizzes
                </Link>

                {/* Analytics */}
                <Link to="/analytics" className="bg-orange-100 p-4 rounded cursor-pointer hover:bg-orange-200 text-gray-700 flex items-center justify-center">
                    View Analytics
                </Link>

            </div>
        </div>
    );
}
