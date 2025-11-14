import React, { useState, useContext } from "react";
import axios from "../api/axios";
import { AuthContext } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Register() {
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: "",
        first_name: "",
        last_name: "",
        role: "student",
    });
    const { login, setUser } = useContext(AuthContext);
    const nav = useNavigate();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const submit = async (e) => {
        e.preventDefault();
        try {
            await axios.post("auth/register/", formData);
            const res = await axios.post("auth/token/", {
                username: formData.username,
                password: formData.password,
            });
            login(res.data);
            const me = await axios.get("auth/me/");
            setUser(me.data);
            nav("/student");
        } catch (err) {
            alert("Registration failed");
            console.error(err);
        }
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-100">
            <form
                className="w-full max-w-md bg-white p-6 rounded shadow"
                onSubmit={submit}
            >
                <h2 className="text-2xl font-bold mb-4">Register</h2>
                <input
                    type="text"
                    name="username"
                    value={formData.username}
                    onChange={handleChange}
                    placeholder="username"
                    className="w-full mb-3 p-2 border rounded"
                    required
                />
                <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    placeholder="email"
                    className="w-full mb-3 p-2 border rounded"
                    required
                />
                <input
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={handleChange}
                    placeholder="password"
                    className="w-full mb-3 p-2 border rounded"
                    required
                />
                <input
                    type="text"
                    name="first_name"
                    value={formData.first_name}
                    onChange={handleChange}
                    placeholder="first name"
                    className="w-full mb-3 p-2 border rounded"
                />
                <input
                    type="text"
                    name="last_name"
                    value={formData.last_name}
                    onChange={handleChange}
                    placeholder="last name"
                    className="w-full mb-3 p-2 border rounded"
                />
                <button className="w-full p-2 bg-blue-600 text-white rounded hover:bg-blue-700">
                    Register
                </button>
            </form>
        </div>
    );
}
