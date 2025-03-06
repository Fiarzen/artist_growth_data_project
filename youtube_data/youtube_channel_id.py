import requests
import json

with open('src/youtube_data/youtube_credentials.json', 'r') as file:
    credentials = json.load(file)
    YOUTUBE_API_KEY = credentials['token']

def get_youtube_channel_id(artist_name):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": artist_name,
        "type": "channel",
        "key": YOUTUBE_API_KEY,
        "maxResults": 1
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "items" in data and data["items"]:
            return data["items"][0]["id"]["channelId"]
        else:
            return None
    else:
        return None

def main():
    artist = input("enter an artist name").strip()
    print(get_youtube_channel_id(artist))

if __name__ == "__main__":
    main()
