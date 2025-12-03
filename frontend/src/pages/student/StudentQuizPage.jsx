import React, { useEffect, useState } from "react";
import api from "../../api/axios";

import { useParams } from "react-router-dom";

export default function StudentQuizPage() {
  const { courseId } = useParams();
  const [course, setCourse] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [score, setScore] = useState(0);

  useEffect(() => {
    loadQuiz();
  }, []);

  const loadQuiz = async () => {
    try {
      const courseRes = await api.get(`/api/courses/${courseId}/`);
      const qRes = await api.get(`/api/courses/${courseId}/questions/`);

      setCourse(courseRes.data);
      setQuestions(qRes.data.questions);
    } catch (err) {
      console.log("Error loading quiz:", err);
    }
  };

  const selectAnswer = (questionId, option) => {
    setAnswers((prev) => ({ ...prev, [questionId]: option }));
  };

  const submitQuiz = async () => {
    let correct = 0;

    questions.forEach((q) => {
      if (answers[q.id] === q.correct_option) {
        correct++;
      }
    });

    setScore(correct);
    setSubmitted(true);

    try {
      await api.post(`/api/courses/${courseId}/save-result/`, {
        score: correct,
        total: questions.length,
      });
      console.log("Quiz result saved");
    } catch (err) {
      console.log("Error saving result:", err);
    }
  };

  if (!course) return <p className="p-6">Loading...</p>;

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-4">Quiz: {course.title}</h1>

      {!submitted ? (
        <div>
          {questions.map((q, index) => (
            <div key={q.id} className="mb-6 p-4 bg-white rounded-lg shadow">
              <p className="font-semibold text-lg">
                {index + 1}. {q.question}
              </p>

              <div className="mt-2 space-y-2">
                {["A", "B", "C", "D"].map((opt) => (
                  <label key={opt} className="flex items-center gap-2 cursor-pointer">
                    <input
                      type="radio"
                      name={`q${q.id}`}
                      value={opt}
                      onChange={() => selectAnswer(q.id, opt)}
                    />
                    {q[`option_${opt.toLowerCase()}`]}
                  </label>
                ))}
              </div>
            </div>
          ))}

          <button
            onClick={submitQuiz}
            className="px-6 py-3 bg-green-600 text-white rounded-lg shadow hover:bg-green-700"
          >
            Submit Quiz
          </button>
        </div>
      ) : (
        <div className="p-6 bg-green-100 rounded-lg shadow mt-6">
          <h2 className="text-2xl font-bold">
            You scored: {score} / {questions.length}
          </h2>
        </div>
      )}
    </div>
  );
}
