from flask import Flask, render_template, request, redirect
import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template("ApiSpotify.html")


@app.route('/playlist', methods=['POST'])
def data_func():
    # Get the username from terminal
    username = str("12141946930")
    scope = 'user-library-read'
    # Erase cache and prompt for user permission
    try:
        token = util.prompt_for_user_token(username, scope, client_id='d15db9a4115746a88af1ee1103431cbc',
                                           client_secret='3a1a060f611f44b4a01c917f66d5bca6',
                                           redirect_uri='http://localhost/')

    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope, client_id='d15db9a4115746a88af1ee1103431cbc',
                                           client_secret='3a1a060f611f44b4a01c917f66d5bca6',
                                           redirect_uri='http://localhost/')

    # Create spotify object with permissions
    spotifyObject = spotipy.Spotify(auth=token)

    searcher = request.form.get("mood")
 

    # Get search results
    searchresults = spotifyObject.search(searcher, 1, 0, "playlist")

    playlist = searchresults['playlists']['items'][0]
    description = playlist['description']
    playlistid = playlist['id']
    playlistcover = spotifyObject.playlist_cover_image(playlistid)
    playlisttracks = spotifyObject.playlist_tracks(playlistid, None, 9, 0, None)
    weblink = (playlist['external_urls']['spotify'])
    
    
    
    return render_template("playlist.html", results=searchresults, mood=searcher,
                           description=description, playlistcover=playlistcover, playlisttracks=playlisttracks,
                           weblink=weblink)


if __name__ == '__main__':
    app.run(debug=True)
