import React from "react";
import ReactPlayer from "react-player";

export default function VideoPlayer({ url }) {
  return (
    <div className="mt-3">
      <ReactPlayer controls url={url} width="100%" />
    </div>
  );
}
