import React, { useState, useContext } from "react";
import axios from "../api/axios";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const { setUser, login } = useContext(AuthContext);
    const nav = useNavigate();

    const submit = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post("/auth/token/", { username, password });
            login(res.data);
            const me = await axios.get("/auth/me/");
            setUser(me.data);
            if (me.data.role === "admin") nav("/admin");
            else nav("/student");
        } catch (err) {
            alert("Login failed");
            console.error(err);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
            <form
                className="w-full max-w-md bg-white p-6 rounded shadow"
                onSubmit={submit}
            >
                <h2 className="text-2xl font-bold mb-4">Login</h2>
                <input
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="username"
                    className="w-full mb-3 p-2 border rounded"
                />
                <input
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    type="password"
                    placeholder="password"
                    className="w-full mb-3 p-2 border rounded"
                />
                <button className="w-full p-2 bg-blue-600 text-white rounded hover:bg-blue-700">
                    Login
                </button>
            </form>
        </div>
    );
}
