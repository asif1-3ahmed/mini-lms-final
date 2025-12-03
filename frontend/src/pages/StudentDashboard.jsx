import React from "react";
import { Link } from "react-router-dom";

export default function StudentDashboard() {
    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold mb-6">Student Dashboard</h1>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-6">

                {/* Courses */}
                <Link to="/student/courses" className="block">
                    <div className="p-6 bg-blue-100 hover:bg-blue-200 rounded-xl shadow cursor-pointer">
                        <h2 className="text-xl font-semibold">Courses</h2>
                        <p className="text-sm mt-2 text-gray-600">
                            View all available courses
                        </p>
                    </div>
                </Link>

                {/* Quiz */}
                <Link to="/student/quiz" className="block">
                    <div className="p-6 bg-yellow-100 hover:bg-yellow-200 rounded-xl shadow cursor-pointer">
                        <h2 className="text-xl font-semibold">Quiz</h2>
                        <p className="text-sm mt-2 text-gray-600">
                            Attempt quizzes for your courses
                        </p>
                    </div>
                </Link>

                {/* Progress */}
                <Link to="/student/progress" className="block">
                    <div className="p-6 bg-green-100 hover:bg-green-200 rounded-xl shadow cursor-pointer">
                        <h2 className="text-xl font-semibold">Progress</h2>
                        <p className="text-sm mt-2 text-gray-600">
                            Track your learning progress
                        </p>
                    </div>
                </Link>

                {/* Certificates */}
                <Link to="/student/certificates" className="block">
                    <div className="p-6 bg-purple-100 hover:bg-purple-200 rounded-xl shadow cursor-pointer">
                        <h2 className="text-xl font-semibold">Certificates</h2>
                        <p className="text-sm mt-2 text-gray-600">
                            Download earned certificates
                        </p>
                    </div>
                </Link>

            </div>
        </div>
    );
}
