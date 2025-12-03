import React, { createContext, useState, useEffect } from "react";
import axios from "../api/axios";

export const AuthContext = createContext();

export function AuthContextProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = (data) => {
    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);
  };

  const logout = () => {
    localStorage.clear();
    setUser(null);
  };

  // Auto-load user if token exists (page refresh)
  useEffect(() => {
    const token = localStorage.getItem("access");
    if (token) {
      fetchUser();
    }
  }, []);

  const fetchUser = async () => {
    try {
      const res = await axios.get("/api/auth/me/");
      setUser(res.data);
    } catch (err) {
      logout();
    }
  };

  return (
    <AuthContext.Provider value={{ user, setUser, login, logout, fetchUser }}>
      {children}
    </AuthContext.Provider>
  );
}

// ✅ Named export constant that matches your main.jsx
export const AuthProvider = AuthContextProvider;
