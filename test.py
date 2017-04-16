# Import the video2gif package
import video2gif
'''
Compile the score function
On the GPU, the network will be using cuDNN layer implementations available in the Lasagne master

If the device is CPU, it will use the CPU version that requires my Lasagne fork with added 3D convolution and pooling.
You can get it from https://github.com/gyglim/Lasagne

'''

score_function = video2gif.get_prediction_function()

from IPython.display import Image, display
import os
from moviepy.editor import VideoFileClip

'''
Now, let's generate generate some GIFs.
For this we create uniform segment of 5 seconds, score them and
finally generate GIFs from the top and bottom scored ones
'''

# Take the example video
video_path='data/nWHIHe-rjoU.mp4'
video_name=os.path.splitext(os.path.split(video_path)[1])[0]
video = VideoFileClip(video_path)

# Build segments (uniformly of 5 seconds)
segmentsArray = []
index = 1
for videoStart in range(0, int(video.duration) - 5, 1):
	print index
	particalSegments = [(start, int(start+video.fps*5)) for start in range(int(videoStart*video.fps),int(video.duration*video.fps),int(video.fps*5))]
	print "particalSegments count:"
	print len(particalSegments)
	segmentsArray.append(particalSegments)
	index = index + 1

print "segments count:"
print len(segmentsArray)

# Score the segments
scores = {}
for particalSegments in segmentsArray:
	particalScores = video2gif.get_scores(score_function, particalSegments, video, stride=8)
	scores.update(particalScores)
	print "score count:"
	print len(scores)

'''
Now we generate GIFs for some segments and show them
'''

# We need a directory to store the GIFs
OUT_DIR='/tmp/gifs'
if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

# Generate GIFs from the top scoring segments
gifCount = len(scores)
print "gifs count:"
print gifCount
good_gifs,bad_gifs = video2gif.generate_gifs(OUT_DIR,scores, video, video_name,top_k=100,bottom_k=3)

# Show them in the jupyter notebook
# for gif_data in good_gifs: # Top GIFs
#     gif_data[1]
#     gif_path='%s/%s_%.2d.gif' % (OUT_DIR,video_name,gif_data[1])
#     with open(gif_path,'rb') as f:
#         display(Image(f.read()), format='png')


# # Now, for comparison, we show the GIFs with the worst scores
# for gif_data in bad_gifs: 
#     gif_data[1]
#     gif_path='%s/%s_%.2d.gif' % (OUT_DIR,video_name,gif_data[1])
#     with open(gif_path,'rb') as f:
#         display(Image(f.read()), format='png')


