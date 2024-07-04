from billboard_manager import BillboardManager
from spotify_manager import SpotifyManager
from pprint import pprint

billboard_manager = BillboardManager()
spotify_manager = SpotifyManager()

# Web Scraping the top 100 songs from Billboard on the chosen date
all_songs = billboard_manager.get_songs()

# Getting a list w/ songs URI's on Spotify
all_songs_uris = spotify_manager.search_songs(
    songs_list=all_songs,
    date=billboard_manager.chosen_year
)

# Creating a Spotify playlist
my_playlist = spotify_manager.create_playlist(
    date=billboard_manager.chosen_year
)

# Adding the top 100 songs to the playlist
spotify_manager.add_songs_to_playlist(
    playlist=my_playlist,
    songs=all_songs_uris,
)
