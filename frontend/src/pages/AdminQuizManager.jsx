import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import "./AdminQuiz.css"; // <-- We will create this file next

export default function AdminQuizManager() {
  const [courses, setCourses] = useState([]);
  const [selectedCourse, setSelectedCourse] = useState("");
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(false);

  const emptyQuestion = {
    question_text: "",
    option_a: "",
    option_b: "",
    option_c: "",
    option_d: "",
    correct_answer: "A",
  };

  // Load courses
  useEffect(() => {
    axios
      .get("/api/courses/")
      .then((res) => setCourses(res.data))
      .catch((err) => console.error(err));
  }, []);

  // Load quiz for selected course
  const loadQuestions = async () => {
    if (!selectedCourse) return;

    setLoading(true);
    try {
      const res = await axios.get(`/api/courses/${selectedCourse}/questions/`);
      setQuestions(res.data);
    } catch (err) {
      setQuestions([]);
    }
    setLoading(false);
  };

  // Add question
  const addQuestion = () => {
    setQuestions([...questions, { ...emptyQuestion }]);
  };

  // Update question
  const updateQuestion = (index, key, value) => {
    const copy = [...questions];
    copy[index][key] = value;
    setQuestions(copy);
  };

  // Delete a question
  const deleteQuestion = (index) => {
    const copy = [...questions];
    copy.splice(index, 1);
    setQuestions(copy);
  };

  // Save quiz
  const saveQuiz = async () => {
    if (!selectedCourse) {
      alert("Please select a course!");
      return;
    }

    try {
      await axios.post(`/api/courses/${selectedCourse}/questions/save/`, {
        questions,
      });
      alert("Quiz saved successfully!");
    } catch (err) {
      alert("Error saving quiz!");
    }
  };

  return (
    <div className="admin-quiz-container">
      <h1 className="title">Create / Manage Quiz</h1>

      {/* Course dropdown */}
      <label>Select Course:</label>
      <select
        className="dropdown"
        value={selectedCourse}
        onChange={(e) => setSelectedCourse(e.target.value)}
      >
        <option value="">-- Select Course --</option>
        {courses.map((c) => (
          <option key={c.id} value={c.id}>
            {c.title}
          </option>
        ))}
      </select>

      <button className="btn load-btn" onClick={loadQuestions}>
        Load Quiz
      </button>

      <button className="btn add-btn" onClick={addQuestion}>
        + Add Question
      </button>

      {loading && <p>Loading...</p>}

      {questions.map((q, i) => (
        <div key={i} className="question-box">
          <h3>Question {i + 1}</h3>

          <input
            type="text"
            className="text-input"
            placeholder="Enter question"
            value={q.question_text}
            onChange={(e) =>
              updateQuestion(i, "question_text", e.target.value)
            }
          />
          <input
            type="text"
            className="text-input"
            placeholder="Option A"
            value={q.option_a}
            onChange={(e) => updateQuestion(i, "option_a", e.target.value)}
          />
          <input
            type="text"
            className="text-input"
            placeholder="Option B"
            value={q.option_b}
            onChange={(e) => updateQuestion(i, "option_b", e.target.value)}
          />
          <input
            type="text"
            className="text-input"
            placeholder="Option C"
            value={q.option_c}
            onChange={(e) => updateQuestion(i, "option_c", e.target.value)}
          />
          <input
            type="text"
            className="text-input"
            placeholder="Option D"
            value={q.option_d}
            onChange={(e) => updateQuestion(i, "option_d", e.target.value)}
          />

          <label>Correct Answer:</label>
          <select
            className="dropdown"
            value={q.correct_answer}
            onChange={(e) =>
              updateQuestion(i, "correct_answer", e.target.value)
            }
          >
            <option value="A">A</option>
            <option value="B">B</option>
            <option value="C">C</option>
            <option value="D">D</option>
          </select>

          <button className="btn delete-btn" onClick={() => deleteQuestion(i)}>
            Delete
          </button>
        </div>
      ))}

      {questions.length > 0 && (
        <button className="btn save-btn" onClick={saveQuiz}>
          Save Quiz
        </button>
      )}
    </div>
  );
}
