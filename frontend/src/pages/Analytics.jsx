import React from "react";

export default function Analytics() {
    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold mb-4">Analytics</h1>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="bg-white p-4 rounded border">
                    <p className="font-semibold">Course Enrollment</p>
                    {/* Charts will go here */}
                </div>
                <div className="bg-white p-4 rounded border">
                    <p className="font-semibold">Student Progress</p>
                    {/* Charts will go here */}
                </div>
            </div>
        </div>
    );
}
