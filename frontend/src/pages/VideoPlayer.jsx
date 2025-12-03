// src/components/VideoPlayer.jsx
import React from "react";
import ReactPlayer from "react-player";

export default function VideoPlayer({ url }) {
    return (
        <div className="w-full max-w-4xl mx-auto">
            <div
                className="player-wrapper relative w-full"
                style={{ paddingBottom: "56.25%" }}
            >
                <ReactPlayer
                    url={url}
                    controls
                    width="100%"
                    height="100%"
                    style={{ position: "absolute", top: 0, left: 0 }}
                />
            </div>
        </div>
    );
}
