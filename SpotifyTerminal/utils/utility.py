import os
from dotenv import load_dotenv

# access environment variables
load_dotenv()

# Get environment variables

# Spotify username
spotify_username = os.getenv("SPOTIFY_USER_NAME")


# Spotify client ID
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")

# Spotify client secret
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Spotify redirect URI
spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

# Spotify scope
spotify_scope = "user-library-read user-modify-playback-state,playlist-modify-private playlist-read-private user-library-read playlist-modify-public"
