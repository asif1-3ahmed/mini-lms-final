import React from "react";
import { useLocation, useParams, useNavigate } from "react-router-dom";

export default function ModuleList() {
  const { id } = useParams();
  const nav = useNavigate();
  const { state } = useLocation();

  const modules = state?.modules || [];
  const courseTitle = state?.courseTitle || "Course";

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
          ← Back to Course
        </button>

        <h1 style={{ color: "#063a6f", fontSize: 32, marginBottom: 10 }}>
          {courseTitle} — Modules
        </h1>

        {modules.length === 0 ? (
          <p style={{ color: "#234e70" }}>No modules available.</p>
        ) : (
          <div style={{ marginTop: 20 }}>
            {modules.map((m, index) => (
              <div
                key={index}
                style={{
                  background: "#ffffff",
                  border: "1px solid #d0eefd",
                  borderRadius: 12,
                  padding: 18,
                  marginBottom: 12,
                  cursor: "pointer",
                  boxShadow: "0 4px 14px rgba(6,58,111,0.06)"
                }}
                onClick={() =>
                  nav(`/courses/${id}/modules/${index + 1}`, {
                    state: { module: m, moduleNumber: index + 1, courseTitle }
                  })
                }
              >
                <h2 style={{ margin: 0, color: "#064a84" }}>
                  Module {index + 1}: {m.title || m}
                </h2>
                <p style={{ color: "#234e70", marginTop: 6 }}>
                  {m.description || "Click to view details"}
                </p>
              </div>
            ))}
          </div>
        )}

      </div>
    </div>
  );
}
