from pytube import Playlist, YouTube
playlist_url = 'https://youtube.com/playlist?list=special_playlist_id'
p = Playlist(playlist_url)
for url in p.video_urls:
    try:
        yt = YouTube(url)
    except yt.exceptions.VideoUnavailable:
        print(f'Video {url} is unavaialable, skipping.')
    else:
        print(f'Downloading video: {url}')
        yt.streams.first().download()
print('[+] all is ok')