from moviepy import editor
video = editor.VideoFileClip("x.mp4")
audio = video.audio
audio.write_audiofile("x.mp3")