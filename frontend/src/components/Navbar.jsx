import React, { useContext, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

export default function Navbar() {
    const { user, logout } = useContext(AuthContext);
    const nav = useNavigate();
    const [menuOpen, setMenuOpen] = useState(false);

    const handleLogout = () => {
        logout();
        nav("/login");
        setMenuOpen(false);
    };

    return (
        <nav className="bg-blue-600 text-white p-4 shadow relative">
            <div className="max-w-7xl mx-auto flex justify-between items-center">
                
                {/* Logo */}
                <Link to="/" className="text-2xl font-bold">
                    Mini LMS
                </Link>

                {/* Hamburger Icon for mobile */}
                <button
                    className="md:hidden text-3xl"
                    onClick={() => setMenuOpen(!menuOpen)}
                >
                    ☰
                </button>

                {/* Desktop Menu */}
                <div className="hidden md:flex gap-4 items-center">
                    {user ? (
                        <>
                            <span>Welcome, {user.username}</span>

                            {user.role === "admin" && (
                                <>
                                    <Link to="/admin" className="hover:bg-blue-700 px-3 py-2 rounded">Admin</Link>
                                    <Link to="/create-course" className="hover:bg-blue-700 px-3 py-2 rounded">Create Course</Link>
                                    <Link to="/upload-video" className="hover:bg-blue-700 px-3 py-2 rounded">Upload Video</Link>
                                    <Link to="/analytics" className="hover:bg-blue-700 px-3 py-2 rounded">Analytics</Link>
                                </>
                            )}

                            {user.role === "student" && (
                                <Link to="/student" className="hover:bg-blue-700 px-3 py-2 rounded">Dashboard</Link>
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
                            <Link to="/login" className="hover:bg-blue-700 px-3 py-2 rounded">Login</Link>
                            <Link to="/register" className="hover:bg-blue-700 px-3 py-2 rounded">Register</Link>
                        </>
                    )}
                </div>
            </div>

            {/* Mobile Slide-in Menu */}
            <div
                className={`
                fixed top-0 right-0 h-full w-64 bg-blue-700 p-6 z-50
                transform transition-transform duration-300
                ${menuOpen ? "translate-x-0" : "translate-x-full"}
                md:hidden
            `}
            >
                {/* Close button */}
                <button
                    className="text-3xl absolute top-4 right-4"
                    onClick={() => setMenuOpen(false)}
                >
                    ✕
                </button>

                <div className="mt-10 flex flex-col gap-4 text-lg">
                    {user ? (
                        <>
                            <span className="text-white">Welcome, {user.username}</span>

                            {user.role === "admin" && (
                                <>
                                    <Link onClick={() => setMenuOpen(false)} to="/admin" className="hover:bg-blue-800 px-3 py-2 rounded">Admin</Link>
                                    <Link onClick={() => setMenuOpen(false)} to="/create-course" className="hover:bg-blue-800 px-3 py-2 rounded">Create Course</Link>
                                    <Link onClick={() => setMenuOpen(false)} to="/upload-video" className="hover:bg-blue-800 px-3 py-2 rounded">Upload Video</Link>
                                    <Link onClick={() => setMenuOpen(false)} to="/analytics" className="hover:bg-blue-800 px-3 py-2 rounded">Analytics</Link>
                                </>
                            )}

                            {user.role === "student" && (
                                <Link onClick={() => setMenuOpen(false)} to="/student" className="hover:bg-blue-800 px-3 py-2 rounded">Dashboard</Link>
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
                            <Link onClick={() => setMenuOpen(false)} to="/login" className="hover:bg-blue-800 px-3 py-2 rounded">Login</Link>
                            <Link onClick={() => setMenuOpen(false)} to="/register" className="hover:bg-blue-800 px-3 py-2 rounded">Register</Link>
                        </>
                    )}
                </div>
            </div>

            {/* Background Overlay when menu is open */}
            {menuOpen && (
                <div
                    className="fixed inset-0 bg-black bg-opacity-50 md:hidden"
                    onClick={() => setMenuOpen(false)}
                ></div>
            )}
        </nav>
    );
}
