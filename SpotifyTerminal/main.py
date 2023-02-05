# Main file

# # Import necessary modules
import utility as util
import current_song as current_track
import play_directly as play_music
import play_based_on_result as play_based_on_search
import add_song_in_specific_playlist as add_track
import remove_specific_song_from_playlist as remove_track
import playlist_search as search_playlist



# Define a function to display the options
def display_options():
    print("Select an option:")
    print("1. Show the current song")
    print("2. Play a song directly")
    print("3. Search for a song and play")
    print("4. Add a track to a playlist")
    print("5. Remove a track from a playlist")
    print("6. Search for a playlist")
    print("7. Quit")

# Call the display_options function
display_options()


while True:
    # Get user's choice
    choice = int(input("Enter your choice (1-7): "))


    # Based on user's choice, call the corresponding function
    if choice == 1:
        current_track.current_song(util.spotify_username, util.spotify_client_id, util.spotify_client_secret, util.spotify_redirect_uri, util.spotify_scope)
    elif choice == 2:
        play_music.play_directly(util.spotify_username, util.spotify_client_id, util.spotify_client_secret, util.spotify_redirect_uri, util.spotify_scope)
    elif choice == 3:
        play_based_on_search.get_top_ten_tracks(util.spotify_username, util.spotify_client_id, util.spotify_client_secret, util.spotify_redirect_uri, util.spotify_scope)
    elif choice == 4:
        add_track.add_song_in_playlist(util.spotify_username, util.spotify_client_id, util.spotify_client_secret, util.spotify_redirect_uri)
    elif choice == 5:
        remove_track.remove_song_from_playlist(util.spotify_username, util.spotify_client_id, util.spotify_client_secret, util.spotify_redirect_uri)
    elif choice == 6:
        search_playlist.search_playlist(util.spotify_username, util.spotify_client_id, util.spotify_client_secret, util.spotify_redirect_uri)
    elif choice == 7:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
        display_options()
