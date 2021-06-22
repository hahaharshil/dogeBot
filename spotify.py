import random

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="775486322f724a04bd149178b80f42fd",
                                               client_secret="4dd2ebb6e15f43948440fa77fa77f9f1",
                                               redirect_uri="http://127.0.0.1:9000/",
                                               scope="user-library-read"
                                               ))


def latest_albums():
    """Returns latest albums
    Returns:
    latest albums
    """
    imp = [
        'id',
        'name',
        'release_date',
        'total_tracks',
        'type',
        'external_urls',
    ]
    limit = 40
    result = sp.new_releases('IN', limit)
    albums = []
    for i in result['albums']['items']:
        albums.append({j: i[j] if j != 'external_urls' else i[j]['spotify'] for j in imp})
    rand = random.randint(0, limit - 1)
    return albums[rand]['external_urls']


def featured_playlists():
    """Return featured playlists
    Returns:
    featured playlists
    """
    limit = 40
    result = sp.featured_playlists(limit=limit)
    playlists = result['playlists']
    final_playlists = [] # Playlists with filtered data
    for i in playlists['items']:
        final_playlists.append({'desc' : i['description'],'external_urls' : i['external_urls']['spotify']})
    rand = random.randint(0, playlists['total'] - 1)
    playlist = final_playlists[rand]
    return f"{playlist['desc']}\n{playlist['external_urls']}"

