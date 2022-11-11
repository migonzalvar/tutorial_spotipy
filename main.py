"""

    export SPOTIPY_CLIENT_ID=...
    export SPOTIPY_CLIENT_SECRET=...
    export SPOTIPY_REDIRECT_URI=http://localhost:8192

"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        # Credenciales de variable de entorno
        scope="user-library-read,playlist-read-private,playlist-modify-private",
    )
)

current_user_r = sp.current_user()
print(current_user_r)
user_id = current_user_r["id"]

playlist_r = sp.user_playlist_create(user_id, "Mi lista desde Python", public=False)
print(playlist_r)

playlist_id = playlist_r["id"]
items = [
    "spotify:track:4cOdK2wGLETKBW3PvgPWqT",
]
item_r = sp.playlist_add_items(playlist_id, items)
print(item_r)

playlists_r = sp.current_user_playlists()
print(f"{playlists_r=}")
for item in playlists_r["items"]:
    print(item["name"], item["uri"])
