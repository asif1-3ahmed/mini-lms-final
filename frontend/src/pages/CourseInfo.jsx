// src/pages/CourseInfo.jsx
import React, { useEffect, useState, useContext } from "react";
import axios from "../api/axios";
import { useParams, useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

/**
 * CourseInfo.jsx
 * Light-blue professional UI (no Tailwind)
 * Admin sees Edit button
 */

export default function CourseInfo() {
  const { id } = useParams();
  const nav = useNavigate();
  const { user } = useContext(AuthContext);
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [openSection, setOpenSection] = useState(null);

  useEffect(() => {
    const load = async () => {
      try {
        const res = await axios.get(`/api/courses/${id}/`);
        const c = res.data || {};

        c.skills = Array.isArray(c.skills) ? c.skills : [];
        c.modules = Array.isArray(c.modules) ? c.modules : [];
        c.career_paths = Array.isArray(c.career_paths) ? c.career_paths : [];
        c.roadmap = Array.isArray(c.roadmap) ? c.roadmap : [];
        c.faq = Array.isArray(c.faq) ? c.faq : [];
        c.videos = Array.isArray(c.videos) ? c.videos : [];

        const enriched = enrichCourse(c);
        setCourse(enriched);
      } catch (err) {
        console.error(err);
        setError("Failed to load course. Check server / network.");
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [id]);

  if (loading)
    return (
      <div style={styles.shell}>
        <div style={styles.container}><p>Loading course…</p></div>
      </div>
    );

  if (error)
    return (
      <div style={styles.shell}>
        <div style={styles.container}>
          <p style={{ color: "#b00020" }}>{error}</p>
        </div>
      </div>
    );

  if (!course) return null;

  return (
    <div style={styles.shell}>
      {/* ---------------- HEADER ---------------- */}
      <div style={styles.header}>
        <div style={styles.headerInner}>
          <div style={styles.brand}>Courses · ManageCourses</div>

          <nav style={styles.nav}>
            <button style={styles.navBtn} onClick={() => nav("/courses")}>
              All courses
            </button>

            <button
              style={styles.navBtn}
              onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
            >
              Top
            </button>

            {user?.role === "admin" && (
              <button
                style={{
                  ...styles.navBtn,
                  background: "#0b78d1",
                  color: "#fff",
                }}
                onClick={() => nav(`/courses/${id}/edit`)}
              >
                Edit course
              </button>
            )}
          </nav>
        </div>
      </div>

      {/* ---------------- MAIN ---------------- */}
      <main style={styles.container}>
        {/* ---------------- HERO ---------------- */}
        <section style={styles.hero}>
          <div>
            <h1 style={styles.title}>{course.title}</h1>
            <p style={styles.lead}>{course.description || course.overview}</p>

            <div style={styles.metaRow}>
              <div style={styles.metaItem}>
                <strong>Duration</strong>
                <div style={styles.metaValue}>
                  {course.duration || "6 - 12 weeks"}
                </div>
              </div>

              <div style={styles.metaItem}>
                <strong>Category</strong>
                <div style={styles.metaValue}>
                  {course.category || "General"}
                </div>
              </div>

              <div style={styles.metaItem}>
                <strong>Level</strong>
                <div style={styles.metaValue}>
                  {course.level || "Beginner → Intermediate"}
                </div>
              </div>
            </div>

            {/* ACTION BUTTONS */}
            <div style={{ marginTop: 16 }}>
              <button
                style={styles.ctaPrimary}
                onClick={() => alert("Enroll flow not implemented yet")}
              >
                Enroll now
              </button>

              <button
                style={styles.ctaGhost}
                onClick={() => alert("Download syllabus not implemented")}
              >
                Download syllabus
              </button>

              {/* ⭐ VIEW MODULES BUTTON ADDED HERE ⭐ */}
              <button
                style={{
                  background: "#ffffff",
                  color: "#0b78d1",
                  border: "1px solid #0b78d1",
                  padding: "10px 16px",
                  borderRadius: 10,
                  cursor: "pointer",
                  fontWeight: 700,
                  marginLeft: 8,
                }}
                onClick={() =>
                  nav(`/courses/${id}/modules`, {
                    state: {
                      modules: course.modules,
                      courseTitle: course.title,
                    },
                  })
                }
              >
                View Modules →
              </button>

              {/* Admin edit inside hero */}
              {user?.role === "admin" && (
                <button
                  style={{
                    ...styles.ctaGhost,
                    marginLeft: 8,
                    borderColor: "#064a84",
                    color: "#064a84",
                  }}
                  onClick={() => nav(`/courses/${id}/edit`)}
                >
                  Edit course
                </button>
              )}
            </div>
          </div>
        </section>

        {/* ---------------- OVERVIEW ---------------- */}
        <section style={styles.card}>
          <h2 style={styles.h2}>Course overview</h2>
          <p style={styles.p}>{course.overview || course.description}</p>

          <h3 style={styles.h3}>What you'll learn</h3>
          <div style={styles.badgeRow}>
            {course.skills.slice(0, 10).map((s, i) => (
              <span key={i} style={styles.badge}>{s}</span>
            ))}
          </div>
        </section>

        {/* ---------------- MODULES ---------------- */}
        <section style={styles.card}>
          <h2 style={styles.h2}>Syllabus & modules</h2>

          {course.modules.length ? (
            <ol>
              {course.modules.map((m, i) => (
                <li key={i} style={styles.listItem}>
                  <div style={styles.moduleTitle}>{m.title || m}</div>
                  {m.description && (
                    <div style={styles.moduleDesc}>{m.description}</div>
                  )}
                </li>
              ))}
            </ol>
          ) : (
            <p style={styles.p}>No modules listed for this course.</p>
          )}
        </section>

        {/* ---------------- PROJECTS ---------------- */}
        <section style={styles.card}>
          <h2 style={styles.h2}>Capstone projects</h2>
          <ul>
            {course.projects.map((p, i) => (
              <li key={i} style={styles.p}>{p}</li>
            ))}
          </ul>
        </section>

        {/* ---------------- CAREER PATHS ---------------- */}
        <section style={styles.card}>
          <h2 style={styles.h2}>Career paths</h2>
          <div style={styles.grid}>
            {course.career_paths.map((c, i) => (
              <div key={i} style={styles.box}>
                <strong>{c}</strong>
                <div style={styles.small}>Industry roles</div>
              </div>
            ))}
          </div>
        </section>

        {/* ---------------- ROADMAP ---------------- */}
        <section style={styles.card}>
          <h2 style={styles.h2}>Learning roadmap</h2>
          <ol>
            {course.roadmap.map((r, i) => (
              <li key={i} style={styles.p}>{r}</li>
            ))}
          </ol>
        </section>

        {/* ---------------- FAQ ---------------- */}
        <section style={styles.card}>
          <h2 style={styles.h2}>FAQ</h2>

          {course.faq.map((f, i) => (
            <div key={i} style={{ marginBottom: 12 }}>
              <button
                onClick={() =>
                  setOpenSection(openSection === i ? null : i)
                }
                style={{
                  ...styles.accordionBtn,
                  ...(openSection === i ? styles.accordionBtnOpen : {}),
                }}
              >
                {f.question}
                <span style={styles.accordionArrow}>
                  {openSection === i ? "−" : "+"}
                </span>
              </button>

              {openSection === i && (
                <div style={styles.accordionPanel}>
                  <p style={styles.p}>{f.answer}</p>
                </div>
              )}
            </div>
          ))}
        </section>

        {/* ---------------- RESOURCES ---------------- */}
        <section style={styles.card}>
          <h2 style={styles.h2}>Resources</h2>
          <ul>
            {course.resources.map((r, i) => (
              <li key={i} style={styles.p}>
                <a href={r.url}>{r.title}</a>
              </li>
            ))}
          </ul>
        </section>
      </main>

      <footer style={styles.footer}>
        <div style={styles.container}>
          <small>© {new Date().getFullYear()} ManageCourses — Blue Theme</small>
        </div>
      </footer>
    </div>
  );
}

/* ============ ENRICH HELPERS — unchanged ============ */
function enrichCourse(c) {
  const title = c.title || "Untitled Course";
  const desc = c.description || c.overview || "";

  const skills = c.skills.length
    ? c.skills
    : generateSkillsFromTitle(title);

  const modules = c.modules.length
    ? c.modules
    : generateModulesFromTitle(title);

  const career_paths = c.career_paths.length
    ? c.career_paths
    : ["Junior Developer", "Project Contributor", "Intern"];

  const roadmap = c.roadmap.length
    ? c.roadmap
    : [
        "Complete modules in order",
        "Finish 3 practical projects",
        "Build portfolio",
        "Submit capstone",
      ];

  const faq = c.faq.length
    ? c.faq
    : [
        { question: "Who is this course for?", answer: "Everyone" },
        { question: "Is certificate provided?", answer: "Yes" },
      ];

  const projects =
    c.projects && c.projects.length
      ? c.projects
      : [
          `Mini project based on ${title}`,
          `Integration project`,
          `Final capstone`,
        ];

  const resources =
    c.resources && c.resources.length
      ? c.resources
      : [
          { title: "Official Docs", url: "#" },
          { title: "Free Tutorials", url: "#" },
        ];

  return {
    ...c,
    title,
    overview: c.overview || desc,
    skills,
    modules,
    career_paths,
    roadmap,
    faq,
    projects,
    resources,
  };
}

function generateSkillsFromTitle(title) {
  const t = title.toLowerCase();
  if (t.includes("python")) return ["Python", "OOP", "Scripting", "Automation"];
  if (t.includes("react")) return ["React", "Hooks", "State", "Routing"];
  if (t.includes("data")) return ["SQL", "EDA", "Visualization", "Pandas"];
  return ["Core concepts", "Hands-on practice", "Real projects"];
}

function generateModulesFromTitle(title) {
  return [
    { title: `Introduction to ${title}`, description: "Basics and setup" },
    { title: `${title} Fundamentals`, description: "Core concepts" },
    { title: `${title} Hands-on`, description: "Real exercises" },
    { title: `Advanced ${title}`, description: "Best practices" },
    { title: `Integrations`, description: "Debug & deploy" },
    { title: `Capstone`, description: "Final project" },
  ];
}

/* ============ STYLES — unchanged ============ */
const styles = {
  shell: {
    fontFamily: "'Segoe UI', Roboto, Arial, sans-serif",
    background: "#f2fbff",
    color: "#0a2540",
    minHeight: "100vh",
    display: "flex",
    flexDirection: "column",
  },
  header: {
    background: "linear-gradient(90deg,#e6f5ff,#cfefff)",
    borderBottom: "1px solid #d6eefc",
    padding: "12px 0",
    position: "sticky",
    top: 0,
    zIndex: 40,
  },
  headerInner: {
    maxWidth: 1100,
    margin: "0 auto",
    display: "flex",
    alignItems: "center",
    justifyContent: "space-between",
    padding: "0 18px",
  },
  brand: {
    fontWeight: 700,
    color: "#064a84",
    fontSize: 16,
  },
  nav: {
    display: "flex",
    gap: 8,
    alignItems: "center",
  },
  navBtn: {
    background: "transparent",
    border: "1px solid transparent",
    padding: "8px 12px",
    borderRadius: 8,
    cursor: "pointer",
    color: "#064a84",
    fontWeight: 600,
  },
  container: {
    maxWidth: 1100,
    margin: "18px auto",
    width: "100%",
    padding: "0 18px",
  },
  hero: {
    display: "flex",
    gap: 20,
    alignItems: "flex-start",
    padding: "18px 0",
  },
  title: {
    fontSize: 32,
    margin: 0,
    color: "#063a6f",
  },
  lead: {
    marginTop: 8,
    color: "#234e70",
    maxWidth: 760,
    lineHeight: 1.45,
  },
  metaRow: {
    display: "flex",
    gap: 12,
    marginTop: 12,
    flexWrap: "wrap",
  },
  metaItem: {
    background: "#e9f6ff",
    padding: "8px 12px",
    borderRadius: 8,
    border: "1px solid #d0eefd",
    minWidth: 120,
  },
  metaValue: {
    marginTop: 6,
    color: "#064a84",
    fontWeight: 700,
  },
  ctaPrimary: {
    background: "#0b78d1",
    color: "#fff",
    border: "none",
    padding: "10px 16px",
    borderRadius: 10,
    cursor: "pointer",
    fontWeight: 700,
    marginRight: 8,
  },
  ctaGhost: {
    background: "transparent",
    color: "#0b78d1",
    border: "1px solid #0b78d1",
    padding: "10px 16px",
    borderRadius: 10,
    cursor: "pointer",
    fontWeight: 700,
  },
  card: {
    background: "#fff",
    border: "1px solid #e0f0fb",
    padding: 18,
    borderRadius: 12,
    marginBottom: 16,
    boxShadow: "0 6px 18px rgba(6,58,111,0.04)",
  },
  h2: {
    margin: "0 0 8px 0",
    color: "#064a84",
    fontSize: 20,
  },
  h3: {
    margin: "6px 0",
    color: "#0b78d1",
  },
  p: {
    color: "#234e70",
    margin: "8px 0",
    lineHeight: 1.5,
  },
  badgeRow: {
    display: "flex",
    gap: 8,
    flexWrap: "wrap",
    marginTop: 8,
  },
  badge: {
    borderRadius: 20,
    border: "1px solid #cce9ff",
    padding: "6px 10px",
    background: "#f0fbff",
    color: "#084a7a",
    fontWeight: 600,
    fontSize: 13,
  },
  listItem: {
    marginBottom: 10,
  },
  moduleTitle: {
    fontWeight: 700,
    color: "#064a84",
  },
  moduleDesc: {
    color: "#234e70",
    marginTop: 6,
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit,minmax(180px,1fr))",
    gap: 12,
  },
  box: {
    background: "#eaf6ff",
    padding: 12,
    borderRadius: 10,
    border: "1px solid #d1ecff",
  },
  small: {
    color: "#235a78",
    fontSize: 12,
    marginTop: 6,
  },
  footer: {
    marginTop: "auto",
    borderTop: "1px solid #e0f0fb",
    padding: "18px 0",
    background: "linear-gradient(180deg,#f6fbff,#eef9ff)",
  },
  accordionBtn: {
    width: "100%",
    textAlign: "left",
    padding: 12,
    borderRadius: 8,
    border: "1px solid #dceefc",
    background: "#f7fdff",
    cursor: "pointer",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    fontWeight: 700,
    color: "#064a84",
  },
  accordionBtnOpen: {
    background: "#0b78d1",
    color: "#fff",
  },
  accordionArrow: {
    fontSize: 18,
    lineHeight: 1,
  },
  accordionPanel: {
    padding: 12,
    borderLeft: "4px solid #e6f5ff",
    marginTop: 8,
    background: "#fff",
    borderRadius: 8,
  },
};
