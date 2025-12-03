import React from "react";
import { Link } from "react-router-dom";

export default function AdminDashboard() {
    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold mb-4">Admin Dashboard</h1>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">

                <Link to="/admin/manage-courses">
                    <div className="bg-blue-100 p-4 rounded cursor-pointer hover:bg-blue-200">
                        <Link to="/admin/manage-courses" className="text-gray-700">
    Manage Courses
</Link>

                    </div>
                </Link>

                <Link to="/upload-video">
                    <div className="bg-green-100 p-4 rounded cursor-pointer hover:bg-green-200">
                        <p className="text-gray-700">Upload Videos</p>
                    </div>
                </Link>

                <Link to="/admin/create-quiz">
                    <div className="bg-purple-100 p-4 rounded cursor-pointer hover:bg-purple-200">
                        <p className="text-gray-700">Create Quizzes</p>
                    </div>
                </Link>

                <Link to="/analytics">
                    <div className="bg-orange-100 p-4 rounded cursor-pointer hover:bg-orange-200">
                        <p className="text-gray-700">View Analytics</p>
                    </div>
                </Link>

            </div>
        </div>
    );
}
