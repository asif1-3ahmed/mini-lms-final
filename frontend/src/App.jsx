import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/Navbar";
import PrivateRoute from "./components/PrivateRoute";

import Login from "./pages/Login";
import Register from "./pages/Register";
import AdminDashboard from "./pages/AdminDashboard";
import StudentDashboard from "./pages/StudentDashboard";
import CourseList from "./pages/CourseList";
import CourseForm from "./pages/CourseForm";
import CourseDetail from "./pages/CourseDetail";
import CourseInfo from "./pages/CourseInfo";
import VideoUpload from "./pages/VideoUpload";
import QuizPage from "./pages/QuizPage";
import Analytics from "./pages/Analytics";
import ManageCourses from "./pages/ManageCourses";
// import these at top
import RoadmapDetail from "./pages/RoadmapDetail";
import ModuleDetail from "./pages/ModuleDetail";
import ModuleList from "./pages/ModuleList";

// inside <Routes> add:


export default function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50">
        
        <Navbar />

        <Routes>

          {/* PUBLIC */}
          <Route path="/" element={<Navigate to="/courses" />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
<Route path="/roadmap/:courseId" element={<RoadmapDetail />} />
<Route path="/courses/:id/modules" element={<ModuleList />} />
<Route path="/courses/:id/modules/:moduleId" element={<ModuleDetail />} />

          {/* PUBLIC COURSE ROUTES */}
          <Route path="/courses" element={<CourseList />} />
          <Route path="/courses/:id" element={<CourseDetail />} />
          <Route path="/courses/:id/info" element={<CourseInfo />} />

          <Route path="/quiz/:id" element={<QuizPage />} />

          {/* STUDENT ONLY */}
          <Route element={<PrivateRoute role="student" />}>
            <Route path="/student" element={<StudentDashboard />} />
          </Route>

          {/* ADMIN ONLY */}
          <Route element={<PrivateRoute role="admin" />}>
            <Route path="/admin" element={<AdminDashboard />} />
            <Route path="/admin/manage-courses" element={<ManageCourses />} />
            <Route path="/courses/new" element={<CourseForm />} />
            <Route path="/courses/:id/edit" element={<CourseForm />} />
            <Route path="/upload-video" element={<VideoUpload />} />
            <Route path="/analytics" element={<Analytics />} />
          </Route>

          {/* FALLBACK */}
          <Route path="*" element={<Navigate to="/login" />} />

        </Routes>

      </div>
    </BrowserRouter>
  );
}
