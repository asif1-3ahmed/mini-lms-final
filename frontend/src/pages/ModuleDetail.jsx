import React from "react";
import { useLocation, useParams, useNavigate } from "react-router-dom";

export default function ModuleDetail() {
  const { id, moduleId } = useParams();
  const nav = useNavigate();
  const { state } = useLocation();

  const module = state?.module;
  const moduleNumber = state?.moduleNumber;
  const courseTitle = state?.courseTitle;

  if (!module)
    return <div style={{ padding: 40 }}>Module not found.</div>;

  return (
    <div style={{
      background: "#f2fbff",
      minHeight: "100vh",
      padding: "30px",
      fontFamily: "'Segoe UI', sans-serif"
    }}>
      <div style={{ maxWidth: 900, margin: "0 auto" }}>

        <button
          onClick={() => nav(-1)}
          style={{
            border: "none",
            background: "transparent",
            color: "#0b78d1",
            fontWeight: 600,
            marginBottom: 20,
            cursor: "pointer"
          }}
        >
          ← Back to Modules
        </button>

        <h1 style={{ color: "#063a6f", fontSize: 32 }}>
          {courseTitle} — Module {moduleNumber}
        </h1>

        <div
          style={{
            marginTop: 20,
            background: "#ffffff",
            border: "1px solid #d0eefd",
            borderRadius: 12,
            padding: 20,
            boxShadow: "0 4px 14px rgba(6,58,111,0.06)"
          }}
        >
          <h2 style={{ color: "#064a84" }}>
            {module.title || module}
          </h2>

          <p style={{ color: "#234e70", marginTop: 10 }}>
            {module.description || "No detailed description available."}
          </p>

          <h3 style={{ marginTop: 20, color: "#0b78d1" }}>Key Concepts</h3>
          <ul>
            <li style={{ color: "#234e70" }}>Core understanding</li>
            <li style={{ color: "#234e70" }}>Real-world application</li>
            <li style={{ color: "#234e70" }}>Mini project</li>
          </ul>
        </div>

      </div>
    </div>
  );
}
