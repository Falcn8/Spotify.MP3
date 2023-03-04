from yt_dlp import YoutubeDL
from eyed3.id3.frames import ImageFrame
import eyed3
import requests

def set_tags(filename:str, artists:list, album_name:str, image_url:str):
    image = requests.get(image_url).content
    audiofile = eyed3.load(filename)
    audiofile.initTag()
    audiofile.tag.artist = ", ".join(artists)
    audiofile.tag.album = album_name
    audiofile.tag.title = filename[9:-4]
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, image, "image/jpg")
    audiofile.tag.save()
    return

def mp3(youtube_url:str, title:str, artists:list, album_name:str, album_image_url:str):
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
        "outtmpl": title,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    filename = title + ".mp3"
    set_tags(filename, artists, album_name, album_image_url)
    return filename
