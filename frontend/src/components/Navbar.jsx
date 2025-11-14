import React, { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

export default function Navbar() {
    const { user, logout } = useContext(AuthContext);
    const nav = useNavigate();

    const handleLogout = () => {
        logout();
        nav("/login");
    };

    return (
        <nav className="bg-blue-600 text-white p-4 shadow">
            <div className="max-w-7xl mx-auto flex justify-between items-center">
                <Link to="/" className="text-2xl font-bold">
                    Mini LMS
                </Link>
                <div className="flex gap-4 items-center">
                    {user ? (
                        <>
                            <span className="text-sm">Welcome, {user.username}</span>
                            {user.role === "admin" && (
                                <>
                                    <Link to="/admin" className="hover:bg-blue-700 px-3 py-2 rounded">
                                        Admin
                                    </Link>
                                    <Link to="/create-course" className="hover:bg-blue-700 px-3 py-2 rounded">
                                        Create Course
                                    </Link>
                                    <Link to="/upload-video" className="hover:bg-blue-700 px-3 py-2 rounded">
                                        Upload Video
                                    </Link>
                                    <Link to="/analytics" className="hover:bg-blue-700 px-3 py-2 rounded">
                                        Analytics
                                    </Link>
                                </>
                            )}
                            {user.role === "student" && (
                                <Link to="/student" className="hover:bg-blue-700 px-3 py-2 rounded">
                                    Dashboard
                                </Link>
                            )}
                            <button
                                onClick={handleLogout}
                                className="bg-red-600 hover:bg-red-700 px-3 py-2 rounded"
                            >
                                Logout
                            </button>
                        </>
                    ) : (
                        <>
                            <Link to="/login" className="hover:bg-blue-700 px-3 py-2 rounded">
                                Login
                            </Link>
                            <Link to="/register" className="hover:bg-blue-700 px-3 py-2 rounded">
                                Register
                            </Link>
                        </>
                    )}
                </div>
            </div>
        </nav>
    );
}
