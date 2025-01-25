import streamlit as st
import pandas as pd
import pickle
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


spotify_song_simi = pickle.load(open('spotify_song_simi.pkl', 'rb'))
spotify_song_dict = pickle.load(open('spotify_song_dict.pkl', 'rb'))
df = pd.DataFrame(spotify_song_dict)

CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

client_credentials_manager = SpotifyClientCredentials(client_id= CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"


st.title('Song Recommendation System')
def spotify_song_recommender(song_name):
    idx = df[df['song']==song_name].index[0]
    songs_list = sorted(enumerate(spotify_song_simi[idx]), reverse=True, key = lambda x:x[1])[1:6]
    song_idx_list =[]
    for i, j in songs_list:
        song_idx_list.append(i)
    simi_song_list = []
    song_poster_url=[]
    for i in song_idx_list:
        simi_song_list.append(df.iloc[i].song)
        song_poster_url.append(get_song_album_cover_url(df.iloc[i].song, df.iloc[i].artist))
    return simi_song_list, song_poster_url


song_name = st.selectbox(
    "Select a song to get recommendations",
    df.song,
)
if st.button('Recommend'):
    song_names, song_poster_url = spotify_song_recommender(song_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(song_names[0])
        st.image(song_poster_url[0])
    with col2:
        st.write(song_names[1])
        st.image(song_poster_url[1])
    with col3:
        st.write(song_names[2])
        st.image(song_poster_url[2])
    with col4:
        st.write(song_names[3])
        st.image(song_poster_url[3])
    with col5:
        st.write(song_names[4])
        st.image(song_poster_url[4])