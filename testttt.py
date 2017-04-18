#-*- coding:utf-8 -*-
'''
Compile the score function
On the GPU, the network will be using cuDNN layer implementations available in the Lasagne master

If the device is CPU, it will use the CPU version that requires my Lasagne fork with added 3D convolution and pooling.
You can get it from https://github.com/gyglim/Lasagne

'''
import os
from moviepy.editor import VideoFileClip
import sys

videosDir = sys.argv[1]

list_dirs = os.walk(videosDir) 
for root, dirs, files in list_dirs:  
  for f in files: 
  	# Take the example video
    video_path = os.path.join(root, f)
    video_name=os.path.splitext(os.path.split(video_path)[1])[0]
    print video_path
    video = VideoFileClip(video_path)
    print "fps:"
    print video.fps