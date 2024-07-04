import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()


class SpotifyManager:

    def __init__(self):
        self._CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
        self._CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
        self._USERNAME = os.getenv("SPOTIFY_USERNAME")
        self._URI = os.getenv("SPOTIFY_URI")
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=self._CLIENT_ID,
                client_secret=self._CLIENT_SECRET,
                redirect_uri=self._URI,
                username=self._USERNAME,
                scope="playlist-modify-public",
                cache_path="token.txt",
                show_dialog=True,
            )
        )
        self._user_id = self.get_user_info()['id']

    def get_user_info(self):
        user = self.sp.current_user()
        return user

    def search_songs(self, songs_list, date):
        results = []
        year = date.split("-")[0]
        for song in songs_list:
            result = self.sp.search(
                q=f"track:{song} year:{year}",
                limit=1,
                type="track",
            )
            try:
                uri = result['tracks']['items'][0]['uri']
                results.append(uri)
            except IndexError:
                print(f"The song '{song}' could not be found.")
        return results

    def create_playlist(self, date):
        new_playlist = self.sp.user_playlist_create(
            user=self._user_id,
            name=f"{date} Billboard 100",
        )
        return new_playlist

    def add_songs_to_playlist(self, playlist, songs: list):
        self.sp.playlist_add_items(
            playlist_id=playlist['id'],
            items=songs
        )

