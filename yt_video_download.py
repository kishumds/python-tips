from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=jNQXAC9IVRw")
yt.title

yt.streams.filter(mime_type="video/mp4", res="360p")[0].download("Inputs & Outputs")