import spotipy
from spotipy.oauth2 import SpotifyOAuth


def add_song_in_playlist(username, client_id, client_secret, redirect_uri):


    # Replace <client_id> and <client_secret> with your Spotify Web API credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-library-read"))




    # Get the list of playlists
    playlists = sp.current_user_playlists()["items"]
    playlist_names = [playlist["name"] for playlist in playlists]

    # Prompt the user to choose a playlist
    print("Choose a playlist to add the track to:")
    for i, playlist_name in enumerate(playlist_names):
        print(f"{i + 1}. {playlist_name}")
    choice = int(input("Enter the number of the playlist: ")) - 1


    # Get the ID of the chosen playlist
    playlist_id = playlists[choice]["id"]

    # show all tracks in a playlist
    results = sp.playlist(playlist_id)
    tracks = results["tracks"]
    # loop through all tracks
    for i, item in enumerate(tracks["items"]):
        track = item["track"]
        print("   %d %32.32s %s" % (i, track["artists"][0]["name"], track["name"]))




    # Find the track by name
    track_name = input("Enter the name of the track: ")
    results = sp.search(track_name, type="track", limit=10)
    tracks = results["tracks"]["items"]

    # Prompt the user to choose a track
    print("Choose a track to add to the playlist:")
    for i, track in enumerate(tracks):
        print(f"{i + 1}. {track['name']} by {track['artists'][0]['name']}")
    choice = int(input("Enter the number of the track: ")) - 1

    # Get the ID of the chosen track
    track_id = tracks[choice]["id"]

    # Add the track to the playlist
    sp.playlist_add_items(playlist_id, [track_id])

    # Confirm that the track was added to the playlist
    results = sp.playlist(playlist_id)
    tracks = results["tracks"]
    for item in tracks["items"]:
        track = item["track"]
        if track["id"] == track_id:
            print(f"Track '{track['name']}' by '{track['artists'][0]['name']}' was added to the playlist.")
            break

