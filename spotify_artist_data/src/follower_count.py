import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

def follower_count(artist_name):
    with open('spotify_credentials.json', 'r') as file:
        credentials = json.load(file)
    client_id = credentials['client_id']
    client_secret = credentials['client_secret'] 
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q=artist_name, type='artist', limit=1)

    if results['artists']['items']:
        artist = results['artists']['items'][0]
        return {"artist": f"{artist['name']}", "followers": artist['followers']['total']}
    else:
        return "Artist not found."

def main():
    print(follower_count())

if __name__ == "__main__":
    main()
