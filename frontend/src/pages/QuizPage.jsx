import React, { useEffect, useState } from "react";
import axios from "../api/axios";

export default function QuizPage({ quizId }) {
    const [quiz, setQuiz] = useState(null);
    const [answers, setAnswers] = useState({});
    const [submitted, setSubmitted] = useState(false);
    const [score, setScore] = useState(0);

    useEffect(() => {
        if (quizId) {
            axios.get(`quizzes/${quizId}/`).then((res) => setQuiz(res.data)).catch(console.error);
        }
    }, [quizId]);

    const submit = () => {
        if (!quiz) return;
        let s = 0;
        quiz.questions.forEach((q) => {
            if ((answers[q.id] || "") === q.correct_option) s++;
        });
        setScore(s);
        setSubmitted(true);
    };

    if (!quiz) return <div className="p-6">Loading...</div>;

    return (
        <div className="p-6 max-w-2xl">
            <h2 className="text-lg font-bold mb-4">{quiz.title}</h2>
            {quiz.questions.map((q) => (
                <div key={q.id} className="mb-4 p-4 border rounded">
                    <p className="font-semibold mb-2">{q.text}</p>
                    {["a", "b", "c", "d"].map((opt) =>
                        q[`option_${opt}`] ? (
                            <label key={opt} className="block mb-2">
                                <input
                                    type="radio"
                                    name={`q${q.id}`}
                                    value={opt}
                                    onChange={() => setAnswers({ ...answers, [q.id]: opt })}
                                    disabled={submitted}
                                    className="mr-2"
                                />
                                {q[`option_${opt}`]}
                            </label>
                        ) : null
                    )}
                </div>
            ))}
            {!submitted && (
                <button
                    className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
                    onClick={submit}
                >
                    Submit
                </button>
            )}
            {submitted && (
                <div className="mt-4 p-4 bg-blue-100 rounded">
                    <p className="text-lg font-semibold">
                        Score: {score} / {quiz.questions.length}
                    </p>
                </div>
            )}
        </div>
    );
}
