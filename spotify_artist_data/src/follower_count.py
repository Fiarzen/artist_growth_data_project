import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from datetime import datetime

def follower_count(artist_name):
    with open('src/spotify_artist_data/spotify_credentials.json', 'r') as file:
        credentials = json.load(file)
    client_id = credentials['client_id']
    client_secret = credentials['client_secret'] 
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    results = sp.search(q=artist_name, type='artist', limit=1)

    if results['artists']['items'][0]['name'] == artist_name:
        artist = results['artists']['items'][0]
        return {"artist": f"{artist['name']}", "followers": artist['followers']['total']}
    else:
        return "Error, artist not found"

def main():
    artist = input("enter an artist name").strip()
    print(follower_count(artist))

if __name__ == "__main__":
    main()
