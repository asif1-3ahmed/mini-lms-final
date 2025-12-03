// src/pages/RoadmapDetail.jsx
import React from "react";
import { Link } from "react-router-dom";

/**
 * RoadmapDetail.jsx
 * - Blue professional theme
 * - Expects `course` prop via location state or you can fetch by id.
 * - For simplicity this example expects a 'course' object from route state or fallback demo data.
 */

const demoCourse = {
  id: "demo-course",
  title: "Data Analytics Path",
  description: "A practical roadmap covering data cleaning, visualization and dashboarding.",
  duration: "12 weeks",
  level: "Beginner → Intermediate",
  modules: [
    { title: "Module 1: Foundations", description: "Python & data basics" },
    { title: "Module 2: Data Wrangling", description: "Pandas, cleaning, joins" },
    { title: "Module 3: Visualization", description: "Charts, dashboards" },
    { title: "Module 4: Capstone", description: "End-to-end project" }
  ],
};

export default function RoadmapDetail({ location }) {
  // If your router provides a course via location.state, use it; otherwise fallback to demoCourse
  const course = (location && location.state && location.state.course) || demoCourse;

  return (
    <div style={styles.page}>
      <div style={styles.container}>
        <header style={styles.header}>
          <div style={styles.brand}>{course.title}</div>
          <p style={styles.lead}>{course.description}</p>
          <div style={styles.metaRow}>
            <div style={styles.meta}>⏱ {course.duration}</div>
            <div style={styles.meta}>🎯 {course.level}</div>
            <Link to="/courses" style={styles.linkBack}>← Back to Courses</Link>
          </div>
        </header>

        <section style={styles.grid}>
          {course.modules.map((m, idx) => (
            <article key={idx} style={styles.card}>
              <h3 style={styles.cardTitle}>Module {idx + 1}: {m.title}</h3>
              <p style={styles.cardDesc}>{m.description}</p>
              <Link
                to={`/roadmap/${encodeURIComponent(course.id)}/module/${idx + 1}`}
                state={{ course }}
                style={styles.cardBtn}
              >
                View module →
              </Link>
            </article>
          ))}
        </section>

        <section style={styles.cta}>
          <h3 style={{ margin: 0 }}>Ready to start?</h3>
          <p style={{ margin: "8px 0 12px", color: "#1f4f78" }}>Jump into Module 1 and begin the hands-on labs.</p>
          <Link to={`/roadmap/${encodeURIComponent(course.id)}/module/1`} state={{ course }} style={styles.startBtn}>
            Start Module 1
          </Link>
        </section>
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    background: "linear-gradient(180deg,#f4fbff,#eaf6ff)",
    fontFamily: "'Segoe UI', Roboto, Arial, sans-serif",
    color: "#08314b",
    padding: "40px 16px",
  },
  container: { maxWidth: 1100, margin: "0 auto" },
  header: { marginBottom: 28 },
  brand: { fontSize: 28, fontWeight: 800, color: "#093a63" },
  lead: { marginTop: 6, color: "#205979", maxWidth: 820 },
  metaRow: { marginTop: 10, display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap" },
  meta: { background: "#e8f6ff", padding: "6px 10px", borderRadius: 8, color: "#104e77", fontWeight: 700 },
  linkBack: { marginLeft: "auto", color: "#0b78d1", textDecoration: "none", fontWeight: 700 },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
    gap: 18,
    marginTop: 20,
  },
  card: {
    background: "#fff",
    borderRadius: 12,
    padding: 18,
    border: "1px solid #e3f3ff",
    boxShadow: "0 8px 20px rgba(6,58,111,0.04)",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    minHeight: 150,
  },
  cardTitle: { fontSize: 16, margin: 0, color: "#083658" },
  cardDesc: { marginTop: 8, color: "#345a6e", flexGrow: 1 },
  cardBtn: {
    marginTop: 12,
    alignSelf: "flex-start",
    padding: "8px 12px",
    background: "#0b78d1",
    color: "#fff",
    borderRadius: 10,
    textDecoration: "none",
    fontWeight: 700,
  },
  cta: {
    marginTop: 28,
    background: "#e8f8ff",
    padding: 20,
    borderRadius: 12,
    border: "1px solid #d7f0ff",
    textAlign: "center",
  },
  startBtn: {
    marginTop: 8,
    padding: "10px 18px",
    background: "#064a84",
    color: "#fff",
    borderRadius: 10,
    textDecoration: "none",
    display: "inline-block",
    fontWeight: 700,
  },
};
