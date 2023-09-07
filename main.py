import os
import time
import ffmpy
from pytube import YouTube

print("Youtube Video Downloader")
time.sleep(1)
videoUrl = YouTube(str(input("Insert youtube video url here:\n>> ")))

response = input("Would you like to download the video as mp4 or mp3?\n>> ")


if response == 'mp4':
    resolution =[int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in videoUrl.streams if i.resolution])))]
    resolution.sort()
    print("These are the available resolutions for the video.")
    print(resolution)
    resolution = input("What resolution would you like?\n>> ") 
    print("Enter your destination (leave blank for current directory)")
    dest = str(input('>> ')) or '.'
    video = videoUrl.streams.filter(res=str(resolution)).first()
    output = video.download(output_path=dest)
    if os.path.splitext(output)[1] != ".mp4":
        ffmpy.FFmpeg(
            inputs={os.path.basename(output): None},
            outputs={os.path.basename(output).replace(str(os.path.splitext(output)[1]), ".mp4"): '-hide_banner -loglevel error'}
        ).run()
        os.remove(output)
elif response == 'mp3':
    print("Enter your destination (leave blank for current directory)")
    dest = str(input('>> ')) or '.'
    video = videoUrl.streams.filter(only_audio=True).first()
    output = video.download(output_path=dest)
    ffmpy.FFmpeg(
        inputs={os.path.basename(output): None},
        outputs={os.path.basename(output).replace(".mp4", ".mp3"): '-hide_banner -loglevel error'}
    ).run()
    os.remove(output)
try:
    print("Downloading video...")
except:
    print("There was an error downloading the video.")
print("Video has downloaded successfully!")
os.system('pause')
