import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import VerticalNavbar from "./components/VerticalNavbar";
import CourseList from "./pages/CourseList";
import CourseDetail from "./pages/CourseDetail";
import Login from "./pages/Login";
import Register from "./pages/Register";
import AdminDashboard from "./pages/AdminDashboard";
import StudentDashboard from "./pages/StudentDashboard";
import ProtectedRoute from "./components/ProtectedRoute";

export default function App(){
  return (
    <div className="min-h-screen flex">
      <VerticalNavbar />
      <main className="flex-1 p-4">
        <Routes>
          <Route path="/login" element={<Login/>} />
          <Route path="/register" element={<Register/>} />
          <Route path="/" element={<Navigate to="/courses" />} />
          <Route path="/courses" element={<CourseList/>} />
          <Route path="/courses/:id" element={<CourseDetail/>} />
          <Route path="/admin" element={<ProtectedRoute role="ADMIN"><AdminDashboard/></ProtectedRoute>} />
          <Route path="/student" element={<ProtectedRoute role="STUDENT"><StudentDashboard/></ProtectedRoute>} />
        </Routes>
      </main>
    </div>
  );
}
