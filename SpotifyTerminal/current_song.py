import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException


def current_song(username, client_id, client_secret, redirect_uri, scope):

    try:
     # Authenticate with Spotify
        auth = SpotifyOAuth(username= username,client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

        sp = spotipy.Spotify(auth_manager=auth)


        # Get the current playback information
        current_playback = sp.current_playback()

        # Check if a track is currently playing
        if current_playback:
            # Get the track name
            track_name = current_playback["item"]["name"]

            # Get the playback progress (in milliseconds)
            progress_ms = current_playback["progress_ms"]

            # Calculate the playback progress (in seconds)
            progress_s = progress_ms / 1000

            # Get the total duration of the track (in milliseconds)
            total_duration_ms = current_playback["item"]["duration_ms"]

            # Calculate the total duration of the track (in seconds)
            total_duration_s = total_duration_ms / 1000

            # Display the track name and its playback information
            print(f"Currently playing: {track_name}")
            print(f"Playback progress: {progress_s:.2f}s / {total_duration_s:.2f}s")
        else:
            # No track is currently playing
            print("No track is currently playing.")
    
    except SpotifyException as e:
    # Handle the SpotifyException
        print(f"An error occurred while getting the current playback information: {e}")
    except Exception as e:
        # Handle any other exception
        print(f"An error occurred: {e}")