import React from "react";
import ReactPlayer from "react-player";

export default function VideoPlayer({ url }){
  return <ReactPlayer url={url} controls width="100%" />;
}
