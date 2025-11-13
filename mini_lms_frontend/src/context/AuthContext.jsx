import React, { createContext, useContext, useState, useEffect } from "react";
import API from "../api/axiosInstance";

const AuthContext = createContext();
export const useAuth = () => useContext(AuthContext);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const raw = localStorage.getItem("user");
    return raw ? JSON.parse(raw) : null;
  });

  useEffect(() => {
    if (user) localStorage.setItem("user", JSON.stringify(user));
    else localStorage.removeItem("user");
  }, [user]);

  const login = async (username, password) => {
    const res = await API.post("/auth/token/", { username, password });
    localStorage.setItem("access_token", res.data.access);
    localStorage.setItem("refresh_token", res.data.refresh);
    const profile = await API.get("/auth/profile/");
    setUser(profile.data);
    return true;
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    setUser(null);
  };

  const registerUser = async (data) => {
    try {
      const res = await API.post("/auth/register/", data);
      return res.status === 201;
    } catch {
      return false;
    }
  };

  return (
    <AuthContext.Provider value={{ user, setUser, login, logout, registerUser }}>
      {children}
    </AuthContext.Provider>
  );
}
