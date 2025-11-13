import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function VerticalNavbar(){
  const { user, logout } = useAuth();
  return (
    <aside className="hidden md:flex flex-col w-64 bg-white border-r">
      <div className="p-4 border-b">
        <h1 className="text-xl font-bold">Mini LMS</h1>
      </div>
      <nav className="p-4 flex-1">
        <Link to="/courses" className="block p-2 rounded hover:bg-gray-100">Courses</Link>
        {user?.role === "ADMIN" && <Link to="/admin" className="block p-2 rounded hover:bg-gray-100">Admin Dashboard</Link>}
        {user?.role === "STUDENT" && <Link to="/student" className="block p-2 rounded hover:bg-gray-100">Student Dashboard</Link>}
      </nav>
      <div className="p-4 border-t">
        {user ? (
          <button onClick={logout} className="w-full p-2 bg-red-500 text-white rounded">Logout</button>
        ) : (
          <Link to="/login" className="w-full block p-2 text-center bg-blue-500 text-white rounded">Login</Link>
        )}
      </div>
    </aside>
  );
}
