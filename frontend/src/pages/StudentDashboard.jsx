import React from "react";

export default function StudentDashboard() {
    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold mb-4">Student Dashboard</h1>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div className="bg-blue-100 p-4 rounded">
                    <p className="font-semibold text-lg">My Courses</p>
                </div>
                <div className="bg-green-100 p-4 rounded">
                    <p className="font-semibold text-lg">My Progress</p>
                </div>
                <div className="bg-purple-100 p-4 rounded">
                    <p className="font-semibold text-lg">Certificates</p>
                </div>
            </div>
        </div>
    );
}
