import React, { createContext, useState, useEffect } from "react";
import axios from "../api/axios";

export const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [user, setUser] = useState(null);

    useEffect(() => {
        const load = async () => {
            const token = localStorage.getItem("access_token");
            if (token) {
                try {
                    const { data } = await axios.get("/auth/me/");
                    setUser(data);
                } catch (err) {
                    console.error(err);
                    setUser(null);
                }
            }
        };
        load();
    }, []);

    const login = (tokens) => {
        localStorage.setItem("access_token", tokens.access);
        localStorage.setItem("refresh_token", tokens.refresh);
    };

    const logout = () => {
        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, setUser, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
}
