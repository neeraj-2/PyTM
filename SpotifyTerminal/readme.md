# SpotifyTerminal

A terminal-based application that allows you to interact with Spotify

# Prerequisites

- Python 3
- Spotipy library
- Spotify account
- Spotify Developer Account
- Client ID and Client Secret from Spotify Developer Dashboard

# Installation

- Clone the repository to your local machine

```
git clone `https://github.com/neeraj-2/PyTM.git`

```

- Go to directory

```
cd SpotifyTerminal
```

- Install required dependencies

```
pip install -r requirements.txt
```

Once the dependencies are installed, create a file named .env in the root directory of the project and add the following information:

```
SPOTIFY_CLIENT_ID=your-client-id
SPOTIFY_CLIENT_SECRET=your-client-secret
SPOTIFY_REDIRECT_URI=your-redirect-uri
SPOTIFY_USER_NAME=your-spotify-username
```

Replace your-client-id, your-client-secret, your-redirect-uri, and your-spotify-username with the actual values from your Spotify Developer account

- Run the application

```
python3 main.py
```

# Usage

The application provides the following options:

- Play a track by name 
- Access User's spotify playlists
- Add/Remove songs in a specific spotify playlist


# Contributing

We welcome contributions to the project! If you have a bug fix or new feature, please create a pull request.

- Fork the repository

- Clone the repository to your local machine

```
git clone `https://github.com/neeraj-2/PyTM.git`

```

- Create a new branch for your changes

```
git checkout -b new-feature
```

- Make the necessary changes
 
- Commit your changes

```
git commit -am "Add new feature"
```

- Push the branch to your remote repository

```
git push origin new-feature
```

- Submit a pull request

Thank you for using this Spotify Terminal App! If you found it helpful, please consider giving it a :heart: by starring the repository on GitHub.
