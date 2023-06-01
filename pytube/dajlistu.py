# dao chatGPT
import pytube
from pytube import Playlist

# Replace the URL below with the URL of the playlist you want to download
playlist_url = 'https://www.youtube.com/playlist?list=PLzMcBGfZo4-ndH9FoC5c5KlwbRRxJz7Gj'

playlist = Playlist(playlist_url)
print(f'Downloading {len(playlist.video_urls)} videos from playlist "{playlist.title}"...')

for video_url in playlist.video_urls:
    video = pytube.YouTube(video_url)    
    print(f'Downloading "{video.title}"...')
    video.streams.first().download()
    
print('Download complete!')
