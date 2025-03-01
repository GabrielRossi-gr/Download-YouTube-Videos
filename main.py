import ssl
import urllib.request
from pytubefix import YouTube
from pytubefix.cli import on_progress

ssl._create_default_https_context = ssl._create_unverified_context

url = input("Digite a URL: ")

destino = "Videos"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download(destino)
