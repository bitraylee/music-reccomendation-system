from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict
import spotipy
import pandas as pd
import os
import cred


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cred.client_ID,client_secret=cred.client_SECRET))


def find_song(name, year):

   """
   This function returns a dataframe with data for a song given the name and release year.
   The function uses Spotipy to fetch audio features and metadata for the specified song.
   
   """
   
   song_data = defaultdict()
   results = sp.search(q= 'track: {} year: {}'.format(name,year), limit=1)
   if results['tracks']['items'] == []:
      return None
   
   results = results['tracks']['items'][0]

   track_id = results['id']
   audio_features = sp.audio_features(track_id)[0]
   
   song_data['name'] = [name]
   song_data['year'] = [year]
   song_data['explicit'] = [int(results['explicit'])]
   song_data['duration_ms'] = [results['duration_ms']]
   song_data['popularity'] = [results['popularity']]
   
   for key, value in audio_features.items():
      song_data[key] = value
   
   return pd.DataFrame(song_data)

# print(find_song("Breaking the habit", 2003))
