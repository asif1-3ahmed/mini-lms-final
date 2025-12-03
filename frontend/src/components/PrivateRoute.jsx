import { Navigate, Outlet } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export default function PrivateRoute({ children, role }) {
  const { user, loading } = useContext(AuthContext);

  // ⛔ Prevent redirect while loading user
  if (loading) return null;

  // 🔹 If no user → redirect to login
  if (!user) return <Navigate to="/login" replace />;

  // 🔹 Multiple roles allowed
  if (Array.isArray(role)) {
    if (!role.includes(user.role)) {
      return <Navigate to="/login" replace />;
    }
    return children || <Outlet />;
  }

  // 🔹 Single role allowed
  if (role && user.role !== role) {
    return <Navigate to="/login" replace />;
  }

  // 🔹 Access granted
  return children || <Outlet />;
}
