from pytube import YouTube
from typer import Typer

app = Typer()


@app.command()
def download_360p_mp4_videos(url: str, outpath: str = "./"):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)


if __name__ == "__main__":
    app()