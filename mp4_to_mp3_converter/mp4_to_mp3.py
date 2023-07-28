from moviepy.editor import *
from tkinter.filedialog import *

link = askopenfilename()

video = VideoFileClip(link)

aud = video.audio



name = link.split("/")
#print(name)
for i in name:
    name2 = i.split(".")
print(name2[0])

aud.write_audiofile(name2[0]+".mp3")