import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

YOUR_APP_CLIENT_ID = "e8eab3d9c63c416e8d6b56af3a2f005e"
YOUR_APP_CLIENT_SECRET = "6d89b5433ef745b487168f035da6fa23"
YOUR_APP_REDIRECT_URI = "http://example.com"



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
                                               client_secret=YOUR_APP_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               )
                     )

user_id = sp.current_user()["id"]

wanted_date = input("Which year you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{wanted_date}")
billBoard_webPage = response.text
# billBoard_webPage

soup = BeautifulSoup(billBoard_webPage, "html.parser")
songs_name = soup.find_all(name="span", class_="chart-element__information__song")

songs = [name.getText() for name in songs_name]
print(songs)