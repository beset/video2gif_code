from IPython.display import Image, display
import os
from moviepy.editor import VideoFileClip
import sys

queue = Queue.Queue(maxsize=500)
sentinel = object()  # guaranteed unique reference

videosDir = sys.argv[1]

list_dirs = os.walk(videosDir) 
for root, dirs, files in list_dirs:  
  for f in files: 
  	# Take the example video
    video_path = os.path.join(root, f)
    video_name=os.path.splitext(os.path.split(video_path)[1])[0].decode('utf-8')
    print video_path
    video = VideoFileClip(video_path)
    
    frames=[]
    seg_nr=0
    for frame_idx, f in enumerate(video.iter_frames()):
        if frame_idx > segments[seg_nr][1]:
            seg_nr+=1
            if seg_nr==len(segments):
                break
            frames=[]

        frames.append(f)

        if len(frames)==16: # Extract scores
            start=time.time()
            snip = model.get_snips(frames,snipplet_mean,0,True)
            queue.put((segments[seg_nr],snip))
            print "put data to queue"
            frames=frames[stride:] # shift by 'stride' frames
    queue.put(sentinel)
        