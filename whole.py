#-*- coding:utf-8 -*-
from IPython.display import Image, display
import os
from moviepy.editor import VideoFileClip

videoPath = './run0414.mp4'


video = VideoFileClip(videoPath)
video_name=os.path.splitext(os.path.split(videoPath)[1])[0].decode('utf-8')
print video_name

clip = video.subclip(20, 620)

print video.fps
clip.write_videofile(video_name + "10fps_01.mp4", fps=10, audio=False)