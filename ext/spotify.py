import requests

def url_to_playlist_id(url:str):
    playlist_id = url.split("/")[-1]
    if "?" in playlist_id:
        playlist_id = playlist_id.split("?")[0]
    return playlist_id

def playlist_validity(playlist_id:str):
    if requests.get(f"https://open.spotify.com/playlist/{playlist_id}").status_code == 200:
        return True
    return False

def playlist_items(playlist_id:str, SPOTIFY_TOKEN:str):
    response = requests.get(f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", headers={"Authorization": "Bearer " + SPOTIFY_TOKEN}).json()
    if "error" in response:
        print(response)
        exit()
    return response["items"]

def tracks(url:str, SPOTIFY_TOKEN:str):
    playlist_id = url_to_playlist_id(url)
    validity = playlist_validity(playlist_id)
    if not validity:
        print("URL is not valid")
        exit()
    items = playlist_items(playlist_id, SPOTIFY_TOKEN)
    result = []
    for track in items:
        track = track["track"]
        track_name = track["name"]
        track_artists = [i["name"] for i in track["artists"]]
        track_album_name = track["album"]["name"]
        track_album_image_url = track["album"]["images"][0]["url"]
        result.append((track_name, track_artists, track_album_name, track_album_image_url))
    return result
