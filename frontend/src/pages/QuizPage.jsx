import React, { useEffect, useState } from "react";
import axios from "../api/axios";
import { useParams } from "react-router-dom";

export default function QuizPage() {
  const { id } = useParams();
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});

  useEffect(() => {
    axios.get(`/api/courses/${id}/quiz/student`)
      .then(res => setQuestions(res.data))
      .catch(err => console.error(err));
  }, [id]);

  const handleSelect = (qId, optionIndex) => {
    setAnswers(prev => ({ ...prev, [qId]: optionIndex }));
  };

  const submitQuiz = () => {
    console.log("Student answers:", answers);
    alert("Quiz submitted!");
  };

  return (
    <div style={{ padding: 20 }}>
      <h1 style={{ fontSize: 26, marginBottom: 20 }}>Quiz</h1>

      {questions.map((q, idx) => (
        <div key={q.id} style={{ marginBottom: 20 }}>
          <h3>{idx + 1}. {q.question}</h3>
          {q.options.map((opt, i) => (
            <label key={i} style={{ display: "block", marginTop: 6 }}>
              <input
                type="radio"
                name={`q-${q.id}`}
                onChange={() => handleSelect(q.id, i)}
              />{" "}
              {opt}
            </label>
          ))}
        </div>
      ))}

      <button
        onClick={submitQuiz}
        style={{
          background: "#0b78d1",
          color: "white",
          padding: "10px 18px",
          borderRadius: 10,
          cursor: "pointer",
          fontWeight: 700,
          marginTop: 20
        }}
      >
        Submit Quiz
      </button>
    </div>
  );
}
