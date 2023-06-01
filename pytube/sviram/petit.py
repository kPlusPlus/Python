from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress

import progressbar as progress

def show_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = bytes_downloaded / total_size * 100
    print(f'Downloading... {progress:.2f}% done')

SAVE_PATH = "P:/YouTube" #to_do

#link of the video to be downloaded
#links= 'http://www.youtube.com/playlist?list=PL2E02D4AF724DC2E5'
links= 'https://www.youtube.com/playlist?list=PL4efVE8mfQDhLsHMHER1Ew--2zGp232qA'

playlist = Playlist(links)

PlayListLinks = playlist.video_urls
N = len(PlayListLinks)
#print('Number of videos in playlist: %s' % len(PlayListLinks))

print(f"This link found to be a Playlist Link with number of videos equal to {N} ")
print(f"\n Lets Download all {N} videos")

for i,link in enumerate(PlayListLinks):
    yt = YouTube(link,on_progress_callback=show_progress)
    d_video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    d_video.download(SAVE_PATH)
    print(i+1, ' Video is Downloaded.')
