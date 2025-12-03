import React, { createContext, useState, useEffect } from "react";
import axios from "../api/axios";

export const AuthContext = createContext();

export function AuthContextProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

 const login = (data) => {
  localStorage.setItem("access", data.access);
  localStorage.setItem("refresh", data.refresh);

  // IMPORTANT: attach token to axios
  axios.defaults.headers.common["Authorization"] = `Bearer ${data.access}`;

  fetchUser();
};


  const logout = () => {
    localStorage.clear();
    setUser(null);
  };

  // Auto-load user on refresh
 useEffect(() => {
  const token = localStorage.getItem("access");

  if (token) {
    axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
    fetchUser();
  } else {
    setLoading(false);
  }
}, []);


  const fetchUser = async () => {
    try {
      const res = await axios.get("/api/auth/me/");
      setUser(res.data);
    } catch (err) {
      logout();
    } finally {
      setLoading(false);
    }
  };

  return (
    <AuthContext.Provider value={{ user, setUser, login, logout, fetchUser, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const AuthProvider = AuthContextProvider;
