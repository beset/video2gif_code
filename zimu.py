#-*- coding:utf-8 -*-
from IPython.display import Image, display
import os
from moviepy.editor import VideoFileClip

zimuPath = './e700.ass'
videoPath = './择天记02.mp4'


video = VideoFileClip(videoPath)
print video.fps


video_name=os.path.splitext(os.path.split(videoPath)[1])[0].decode('utf-8')
print video_name
print videoPath
video = VideoFileClip(videoPath)
print "fps:"
print video.fps

clip = video.subclip('0:00:14.88', '0:00:17.28')
out_gif = "%s/%s_%.2d.gif" % ('./gifs', video_name, 1)
print out_gif
# clip = clip.resize(width=500)
# clip.write_gif(out_gif, fps=10)
clip = clip.resize(height=240)
clip.write_gif(out_gif, fps=5)



# zimus = []
# zimuFile = open(zimuPath)
# line = zimuFile.readline()
# while line:
#     if line.startswith("Dialogue"):
#         start = ""
#         end = ""
#         content = ""
#         coms = line.split(",")
#         if len(coms) >= 3:
#             start = coms[1]
#             end = coms[2]

#         coms2 = line.split(",,")
#         if len(coms2) >= 2:
#             content = unicode(coms2[1].strip(), "utf-8")
#         if start == "" or end == "" or content == "" or len(content) > 10:
#             line = zimuFile.readline()
#             continue

#         zimu = {"start": start, "end": end, "content":content}
#         print zimu
#         zimus.append(zimu)
#     line = zimuFile.readline()

# zimuFile.close()

# out_dir = "./gifs"
# video_id = "s700"
# nr = 0
# for zimu in zimus:
#     # clip = video.subclip(zimu['start'], zimu['end'])
#     clip = video.subclip('0:00:14.88', '0:00:17.28')
#     print zimu['start']
#     print zimu['end']
#     out_gif = "%s/%s_%.2d.gif" % (out_dir, video_id, nr)
#     clip = clip.resize(height=240)
#     clip.write_gif(out_gif, fps=5)
#     print "add one gif"
#     nr = nr + 1
