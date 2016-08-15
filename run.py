import urllib.request
import os
import pafy

# Open YouTube URL and create a directory for the mix
url = input("Youtube URL: ").strip()
video = pafy.new(url)
os.makedirs(video.title)

# Download the audio and the cover art
bestaudio = video.getbestaudio(preftype="m4a")
bestaudio.download(quiet=False, filepath=video.title+"/")
urllib.request.urlretrieve(video.bigthumbhd, video.title+"/cover-art.jpg")

