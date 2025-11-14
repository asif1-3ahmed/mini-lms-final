import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

export default function VerticalNavbar() {
  const { user, logout } = useContext(AuthContext);

  if (!user) return null;

  return (
    <div className="w-64 bg-white shadow-md min-h-screen p-4">
      <h1 className="text-2xl font-bold mb-6">Mini LMS</h1>

      <nav className="flex flex-col space-y-3">

        <Link className="text-blue-600" to="/courses">
          Courses
        </Link>

        {user.role === "ADMIN" && (
          <Link className="text-blue-600" to="/admin">
            Admin Dashboard
          </Link>
        )}

        {user.role === "STUDENT" && (
          <Link className="text-blue-600" to="/student">
            Student Dashboard
          </Link>
        )}

        <button
          className="mt-8 bg-red-500 text-white px-4 py-2 rounded"
          onClick={logout}
        >
          Logout
        </button>
      </nav>
    </div>
  );
}
