import { Navigate, Outlet } from "react-router-dom";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export default function PrivateRoute({ children, role }) {
  const { user } = useContext(AuthContext);

  if (!user) {
    return <Navigate to="/login" />;
  }

  // ✅ Allow multiple roles
  if (Array.isArray(role)) {
    if (!role.includes(user.role)) {
      return <Navigate to="/login" />;
    }
    return children ? children : <Outlet />;
  }

  // ✅ Allow single role
  if (user.role !== role) {
    return <Navigate to="/login" />;
  }

  return children ? children : <Outlet />;
}
