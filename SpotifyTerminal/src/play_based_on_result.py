import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Request authorization to access your Spotify account
scope = "user-library-read user-modify-playback-state,playlist-modify-private playlist-read-private user-library-read playlist-modify-public"

def get_top_ten_tracks(username, client_id, client_secret, redirect_uri, scope):
    

    # Authenticate with Spotify
    auth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
    sp = spotipy.Spotify(auth_manager=auth)

    # Get the search query from the user
    query = input("Enter the name of the track you want to play: ")



    # Search for tracks matching the query
    results = sp.search(query, type="track", limit=10)
    tracks = results["tracks"]["items"]

    # Print the list of tracks
    for i, track in enumerate(tracks):
        print(f"{i + 1}. {track['name']} by {track['artists'][0]['name']}")

    # Get the index of the track the user wants to play
    selected_index = int(input("Enter the number of the track you want to play: ")) - 1

    # Get the track id for the selected track
    track_id = tracks[selected_index]["id"]

    # Play the selected track
    sp.start_playback(uris=[f"spotify:track:{track_id}"])

    # Confirm that the track is playing
    results = sp.current_playback()
    current_track = results["item"]
    print(f"Now playing: {current_track['name']} by {current_track['artists'][0]['name']}")