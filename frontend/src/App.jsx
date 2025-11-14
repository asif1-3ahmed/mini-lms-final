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
import VideoUpload from "./pages/VideoUpload";
import QuizPage from "./pages/QuizPage";
import Analytics from "./pages/Analytics";

function App() {
    return (
        <BrowserRouter>
            <div className="min-h-screen bg-gray-50">
                <Navbar />
                <Routes>
                    <Route path="/" element={<Navigate to="/courses" />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/register" element={<Register />} />

                    <Route element={<PrivateRoute />}>
                        <Route path="/student" element={<StudentDashboard />} />
                        <Route path="/courses" element={<CourseList />} />
                        <Route path="/courses/new" element={<CourseForm />} />
                        <Route path="/courses/:id" element={<CourseDetail />} />
                        <Route path="/quiz/:id" element={<QuizPage />} />
                    </Route>

                    <Route element={<PrivateRoute role="admin" />}>
                        <Route path="/admin" element={<AdminDashboard />} />
                        <Route path="/upload-video" element={<VideoUpload />} />
                        <Route path="/analytics" element={<Analytics />} />
                    </Route>
                </Routes>
            </div>
        </BrowserRouter>
    );
}

export default App;