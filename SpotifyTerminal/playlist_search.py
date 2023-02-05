import spotipy
from spotipy.oauth2 import SpotifyOAuth


def search_playlist(username, client_id, client_secret, redirect_uri):


    # Replace <client_id> and <client_secret> with your Spotify Web API credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-library-read"))




    # Get the list of playlists
    playlists = sp.current_user_playlists()["items"]
    playlist_names = [playlist["name"] for playlist in playlists]

    # Prompt the user to choose a playlist
    print("Here are your playlists:")
    for i, playlist_name in enumerate(playlist_names):
        print(f"{i + 1}. {playlist_name}")
    choice = int(input("Enter the number of the playlist to search: ")) - 1


    # Get the ID of the chosen playlist
    playlist_id = playlists[choice]["id"]

    # show all tracks in a playlist
    results = sp.playlist(playlist_id)
    tracks = results["tracks"]
    # loop through all tracks
    for i, item in enumerate(tracks["items"]):
        track = item["track"]
        print("   %d %32.32s %s" % (i, track["artists"][0]["name"], track["name"]))

