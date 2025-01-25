import streamlit as st
import pickle
import numpy as np
import pandas as pd
import requests


api_key = 'aeee4f279100d05b4e93933542d625b3'

movie_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
movie_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl', "rb"))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}'.format(movie_id, api_key))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommendations(movie_name):
    # st.write(movie_name)
    idx = movies[movies['title']==movie_name].index[0]
    similar_movies_idx = sorted(list(enumerate(similarity[idx])), reverse=True, key= lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_id = []
    recommended_movies_poster =[]
    for i in similar_movies_idx:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_id.append(movies.iloc[i[0]].movie_id)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, recommended_movies_poster


st.title('Movie Recomendation System')
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movie_list,
)
if st.button("Recommend", key = "primary"):
    names, poster= recommendations(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(names[0])
        st.image(poster[0])

    with col2:
        st.write(names[1])
        st.image(poster[1])

    with col3:
        st.write(names[2])
        st.image(poster[2])

    with col4:
        st.write(names[3])
        st.image(poster[3])

    with col5:
        st.write(names[4])
        st.image(poster[4])
