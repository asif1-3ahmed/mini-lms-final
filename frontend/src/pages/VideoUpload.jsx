import React, { useState, useEffect } from "react";
import { storage, ref, uploadBytesResumable, getDownloadURL } from "../firebase";
import axios from "../api/axios";

export default function VideoUpload() {
    const [file, setFile] = useState(null);
    const [title, setTitle] = useState("");
    const [desc, setDesc] = useState("");
    const [courseId, setCourseId] = useState("");
    const [courses, setCourses] = useState([]);
    const [uploading, setUploading] = useState(false);

    useEffect(() => {
        axios.get("courses/").then((res) => setCourses(res.data.results || res.data)).catch(console.error);
    }, []);

    const upload = () => {
        if (!file) return alert("Choose a file");
        if (!courseId) return alert("Select a course");

        setUploading(true);
        const storageRef = ref(storage, `videos/${Date.now()}_${file.name}`);
        const uploadTask = uploadBytesResumable(storageRef, file);

        uploadTask.on(
            "state_changed",
            (snapshot) => {
                const progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
                console.log("Upload is " + progress + "% done");
            },
            (error) => {
                console.error(error);
                alert("Upload failed");
                setUploading(false);
            },
            async () => {
                const url = await getDownloadURL(uploadTask.snapshot.ref);
                await axios.post("videos/", {
                    course: courseId,
                    title,
                    description: desc,
                    storage_url: url,
                });
                alert("Uploaded & saved");
                setFile(null);
                setTitle("");
                setDesc("");
                setCourseId("");
                setUploading(false);
            }
        );
    };

    return (
        <div className="p-6 max-w-md">
            <h2 className="text-lg font-bold mb-3">Upload Video</h2>
            <input
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Video title"
                className="w-full p-2 border mb-2 rounded"
            />
            <textarea
                value={desc}
                onChange={(e) => setDesc(e.target.value)}
                placeholder="Video description"
                className="w-full p-2 border mb-2 rounded"
            />
            <select
                value={courseId}
                onChange={(e) => setCourseId(e.target.value)}
                className="w-full p-2 border mb-2 rounded"
            >
                <option value="">Select Course</option>
                {courses.map((c) => (
                    <option value={c.id} key={c.id}>
                        {c.title}
                    </option>
                ))}
            </select>
            <input
                type="file"
                accept="video/*"
                onChange={(e) => setFile(e.target.files[0])}
                className="mb-2"
            />
            <button
                onClick={upload}
                disabled={uploading}
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:bg-gray-400"
            >
                {uploading ? "Uploading..." : "Upload"}
            </button>
        </div>
    );
}
