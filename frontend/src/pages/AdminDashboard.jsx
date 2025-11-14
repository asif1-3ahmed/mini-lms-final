import React from "react";  

export default function AdminDashboard() {
    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold mb-4">Admin Dashboard</h1>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div className="bg-blue-100 p-4 rounded">
                    <p className="text-gray-700">Manage Courses</p>
                </div>
                <div className="bg-green-100 p-4 rounded">
                    <p className="text-gray-700">Upload Videos</p>
                </div>
                <div className="bg-purple-100 p-4 rounded">
                    <p className="text-gray-700">Create Quizzes</p>
                </div>
                <div className="bg-orange-100 p-4 rounded">
                    <p className="text-gray-700">View Analytics</p>
                </div>
            </div>
        </div>
    );
}
