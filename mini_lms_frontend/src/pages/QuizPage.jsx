import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "../api/axiosInstance";

export default function QuizPage() {
  const { quizId } = useParams();
  const [quiz, setQuiz] = useState(null);
  const [answers, setAnswers] = useState({});
  const [score, setScore] = useState(null);

  useEffect(() => {
    axios.get(`/quizzes/${quizId}/`).then((res) => setQuiz(res.data));
  }, [quizId]);

  const choose = (qId, opt) => setAnswers(prev => ({...prev, [qId]: opt}));

  const submit = async () => {
    // call evaluate endpoint or evaluate client-side if correct field provided
    const res = await axios.post(`/quizzes/${quizId}/submit/`, {answers});
    setScore(res.data.score);
  };

  if (!quiz) return <p>Loading...</p>;

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">{quiz.title}</h1>

      {quiz.questions.map(q => (
        <div key={q.id} className="bg-white p-4 rounded mb-3 shadow">
          <p className="font-semibold">{q.text}</p>
          <div className="mt-2 space-y-2">
            {["option_a","option_b","option_c","option_d"].map((opt,labelIdx) => {
              const text = q[opt];
              if (!text) return null;
              const code = opt.split("_")[1] || "a";
              return (
                <label key={opt} className="flex items-center gap-2">
                  <input type="radio" checked={answers[q.id]===code} onChange={()=>choose(q.id, code)} />
                  <span>{text}</span>
                </label>
              );
            })}
          </div>
        </div>
      ))}

      <button onClick={submit} className="bg-green-600 text-white px-4 py-2 rounded">Submit</button>

      {score !== null && <div className="mt-4">Score: {score}</div>}
    </div>
  );
}
