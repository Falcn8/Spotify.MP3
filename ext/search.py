import requests

def generate_query(title:str, artists:str):
    query = title
    for artist in artists:
        if not artist.lower() in title.lower():
            query += " " + artist
    return query + " Lyrics"

def get_videos(query:str):
    videos = []
    headers = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    url = "https://www.youtube.com/results"
    response = requests.get(url, params={"search_query": query}, headers=headers).text
    while response.find("/watch?v=") != -1:
        index = response.find("/watch?v=")
        video = "https://www.youtube.com" + response[index:index+20]
        videos.append(video)
        response = response[index+20:]
    return videos

def YouTube(title:str, artists:str):
    query = generate_query(title, artists)
    video = get_videos(query)[0]
    return video
