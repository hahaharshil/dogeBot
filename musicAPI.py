import random

import spotipy
from spotipy import oauth2


class spotify:
    def __init__(self):
        token = oauth2.SpotifyClientCredentials(client_id="775486322f724a04bd149178b80f42fd",
                                                     client_secret="4dd2ebb6e15f43948440fa77fa77f9f1")
        cache_token = token.get_access_token(as_dict=False)
        self.sp = spotipy.Spotify(cache_token)

    def latest_albums(self):
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
        result = self.sp.new_releases('IN', limit)
        albums = []
        for i in result['albums']['items']:
            albums.append({j: i[j] if j != 'external_urls' else i[j]['spotify'] for j in imp})
        rand = random.randint(0, limit - 1)
        return albums[rand]['external_urls']

    def featured_playlists(self):
        """Return featured playlists
        Returns:
        featured playlists
        """
        limit = 40
        result = self.sp.featured_playlists(limit=limit)
        playlists = result['playlists']
        final_playlists = []  # Playlists with filtered data
        for i in playlists['items']:
            final_playlists.append({'desc': i['description'], 'external_urls': i['external_urls']['spotify']})
        rand = random.randint(0, playlists['total'] - 1)
        playlist = final_playlists[rand]
        return f"{playlist['desc']}\n{playlist['external_urls']}"
if __name__ == "__main__":
    sp = spotify()
    print(sp.latest_albums())
