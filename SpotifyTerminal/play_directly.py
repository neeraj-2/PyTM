import spotipy
import spotipy.util as util

def play_directly(username, client_id, client_secret, redirect_uri, scope):

    # Request authorization to access your Spotify account
    scope = "user-library-read user-modify-playback-state"
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    # Create a Spotify client object
    sp = spotipy.Spotify(auth=token)

    # Search for a song
    query = input("Enter a song to play: ")
    results = sp.search(query, type="track", limit=1)

    # Get the first song from the search results
    song = results["tracks"]["items"][0]
    print("Playing: " + song["name"])

    # Play the song
    sp.start_playback(uris=[song["uri"]])

