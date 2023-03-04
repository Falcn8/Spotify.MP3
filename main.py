import ext.audio as audio
import ext.search as search
import ext.spotify as spotify

SPOTIFY_TOKEN = "YOUR_SPOTIFY_OAUTH_KEY"

def main():
    print("~~~ Spotify.MP3 ~~~\nBy using this program, you hereby consent to our disclaimer and agree to its terms.\n")
    url = input("Enter Spotify playlist URL: ")
    print("Downloading...")
    tracks = spotify.tracks(url, SPOTIFY_TOKEN)
    output_dir = "output/"
    for n, track in enumerate(tracks):
        video = search.YouTube(track[0], track[1])
        audio.mp3(video, output_dir+str(n+1)+"."+track[0], track[1], track[2], track[3])
    print("Downloaded all tracks")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborting...")
