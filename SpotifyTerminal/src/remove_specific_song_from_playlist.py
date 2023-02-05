import spotipy
from spotipy.oauth2 import SpotifyOAuth



def remove_song_from_playlist(username, client_id, client_secret, redirect_uri):

    # Replace <client_id> and <client_secret> with your Spotify Web API credentials
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= client_id,
                                                client_secret= client_secret,
                                                redirect_uri= redirect_uri,
                                                scope=["playlist-modify-private", "playlist-read-private", "user-library-read","playlist-modify-public"]))



    # Search for the playlists of the user
    results = sp.user_playlists(username)
    playlists = results["items"]

    # show all playlists
    while results["next"]:
        results = sp.next(results)
        playlists.extend(results["items"])

    # Print the playlist names
    for playlist in playlists:
        print(playlist["name"])


    # Search for a specific playlist
    # take the name of the playlist as input
    playlist_name = input("Enter the name of the playlist: ")

    # Search for the playlists of the user



    # Find the desired playlist by name
    playlist_id = None
    for playlist in playlists:
        if playlist["name"] == playlist_name:
            playlist_id = playlist["id"]
            break

    # Print the playlist ID if it was found
    if playlist_id:
        print("Playlist ID:", playlist_id)
    else:
        print("Playlist not found.")


    # show all tracks in a playlist
    results = sp.playlist(playlist_id)
    tracks = results["tracks"]
    # loop through all tracks
    for i, item in enumerate(tracks["items"]):
        track = item["track"]
        print("   %d %32.32s %s" % (i, track["artists"][0]["name"], track["name"]))

        

    # Search for a specific track in a playlist
    # take the name of the track as input
    track_name = input("Enter the name of the track: ")

    # Search for the tracks in the playlist
    results = sp.playlist(playlist_id)
    tracks = results["tracks"]

    # Find the desired track by name
    track_id = None

    for item in tracks["items"]:
        track = item["track"]
        if track["name"] == track_name:
            track_id = track["id"]
            break

    # Print the track ID if it was found
    if track_id:
        print("Track ID:", track_id)
    else:
        print("Track not found.")

    # show track details
    track = sp.track(track_id)
    print(track["name"] + " - " + track["artists"][0]["name"])

    # remove track from playlist
    sp.playlist_remove_all_occurrences_of_items(playlist_id, [track_id])

    # show success message
    print("Track removed from playlist.")

    # message to show updated playlist
    print("Updated playlist:")

    # show updated playlist
    results = sp.playlist(playlist_id)
    tracks = results["tracks"]
    # loop through all tracks
    for i, item in enumerate(tracks["items"]):
        track = item["track"]
        print("   %d %32.32s %s" % (i, track["artists"][0]["name"], track["name"]))





