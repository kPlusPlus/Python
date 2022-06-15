from pytube import YouTube
#YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=8bnfcXixwqs&list=RD5whtU7mxeag&index=3')
yt.streams.filter(progressive=True, file_extension='mp4')
yt.streams.order_by('resolution')
yt.streams.desc()
#yt.streams.first()
print(yt.streams)
yt.streams.first().download()

