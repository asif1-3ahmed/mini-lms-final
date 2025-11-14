import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";

import VerticalNavbar from "./components/VerticalNavbar";
import PrivateRoute from "./components/PrivateRoute";

import Login from "./pages/Login";
import Register from "./pages/Register";

import CourseList from "./pages/CourseList";
import CourseDetail from "./pages/CourseDetail";
import CourseForm from "./pages/CourseForm";

import AdminDashboard from "./pages/AdminDashboard";
import StudentDashboard from "./pages/StudentDashboard";
import QuizPage from "./pages/QuizPage";

export default function App() {
  const user = JSON.parse(localStorage.getItem("user"));

  const isLoggedIn = Boolean(user?.token);

  const renderLayout = (page) => {
    // If not logged in → no navbar
    if (!isLoggedIn) return page;

    // If logged in → show navbar + page
    return (
      <div className="min-h-screen flex bg-gray-100">
        <VerticalNavbar />
        <main className="flex-1 p-6">{page}</main>
      </div>
    );
  };

  return (
    <Routes>
      {/* ---------- AUTH ---------- */}
      <Route path="/login" element={renderLayout(<Login />)} />
      <Route path="/register" element={renderLayout(<Register />)} />

      {/* ---------- ROOT REDIRECT ---------- */}
      <Route
        path="/"
        element={
          isLoggedIn
            ? user.role === "ADMIN"
              ? <Navigate to="/admin" />
              : <Navigate to="/student" />
            : <Navigate to="/login" />
        }
      />

      {/* ---------- STUDENT AREA ---------- */}
      <Route
        path="/student"
        element={
          renderLayout(
            <PrivateRoute role="STUDENT">
              <StudentDashboard />
            </PrivateRoute>
          )
        }
      />

      <Route
        path="/courses"
        element={renderLayout(<CourseList />)}
      />

      <Route
        path="/courses/:id"
        element={renderLayout(<CourseDetail />)}
      />

      <Route
        path="/quiz/:quizId"
        element={renderLayout(<QuizPage />)}
      />

      {/* ---------- ADMIN AREA ---------- */}
      <Route
        path="/admin"
        element={
          renderLayout(
            <PrivateRoute role="ADMIN">
              <AdminDashboard />
            </PrivateRoute>
          )
        }
      />

      <Route
        path="/admin/course/new"
        element={
          renderLayout(
            <PrivateRoute role="ADMIN">
              <CourseForm />
            </PrivateRoute>
          )
        }
      />

      <Route
        path="/admin/course/edit/:id"
        element={
          renderLayout(
            <PrivateRoute role="ADMIN">
              <CourseForm />
            </PrivateRoute>
          )
        }
      />

      {/* fallback */}
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
}
