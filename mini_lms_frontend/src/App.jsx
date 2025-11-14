import React from "react";
import { Routes, Route, Navigate, useLocation } from "react-router-dom";
import VerticalNavbar from "./components/VerticalNavbar";
import CourseList from "./pages/CourseList";
import CourseDetail from "./pages/CourseDetail";
import Login from "./pages/Login";
import Register from "./pages/Register";
import AdminDashboard from "./pages/AdminDashboard";
import StudentDashboard from "./pages/StudentDashboard";
import ProtectedRoute from "./components/PrivateRoute";

export default function App() {
  const location = useLocation();
  const hideNavbar = ["/login", "/register"].includes(location.pathname);

  return (
    <div className="min-h-screen flex bg-gray-100">

      {/* Sidebar only when logged in */}
      {!hideNavbar && <VerticalNavbar />}

      <main className="flex-1 p-4">
        <Routes>

          {/* Auth pages */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          {/* Homepage → Login */}
          <Route path="/" element={<Navigate to="/login" replace />} />

          {/* Courses (public browse allowed) */}
          <Route path="/courses" element={<CourseList />} />
          <Route path="/courses/:id" element={<CourseDetail />} />

          {/* Dashboards (protected) */}
          <Route
            path="/admin"
            element={
              <ProtectedRoute role="ADMIN">
                <AdminDashboard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/student"
            element={
              <ProtectedRoute role="STUDENT">
                <StudentDashboard />
              </ProtectedRoute>
            }
          />

          {/* Catch-all → Login */}
          <Route path="*" element={<Navigate to="/login" replace />} />

        </Routes>
      </main>
    </div>
  );
}
