#-*- coding:utf-8 -*-
from moviepy.editor import VideoFileClip
import os

zimuPath = './e700.ass'
videoPath = './e700.rmvb'

video = VideoFileClip(videoPath)

zimus = []
zimuFile = open(zimuPath)
line = zimuFile.readline()
while line:
    if line.startswith("Dialogue"):
        start = ""
        end = ""
        content = ""
        coms = line.split(",")
        if len(coms) >= 3:
            start = coms[1]
            end = coms[2]

        coms2 = line.split(",,")
        if len(coms2) >= 2:
            content = unicode(coms2[1].strip(), "utf-8")
        if start == "" or end == "" or content == "" or len(content) > 10:
            line = zimuFile.readline()
            continue

        zimu = {"start": start, "end": end, "content":content}
        print zimu
        zimus.append(zimu)
    line = zimuFile.readline()

zimuFile.close()

out_dir = "./gifs"
video_id = "s700"
nr = 0
for zimu in zimus:
    clip = video.subclip(zimu['start'], zimu['end'])
    out_gif = "%s/%s_%.2d.gif" % (out_dir, video_id, nr)
    clip = clip.resize(height=240)
    clip.write_gif(out_gif, fps=10)
    print "add one gif"
    nr = nr + 1
