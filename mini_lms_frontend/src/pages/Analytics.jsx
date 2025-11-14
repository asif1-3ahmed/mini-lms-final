import React from "react";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function Analytics({ data }) {
  // data = [{date: '2025-11-01', progress: 20}, ...]
  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="progress" stroke="#8884d8" />
      </LineChart>
    </ResponsiveContainer>
  );
}
