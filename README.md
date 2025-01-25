# Movie Song Recommendation System
Made an app that contains two section:
## Movie recommender section
A movie recomender section where you user can type a movie name and will get the similiar movie names based on similarity between them such as cast, crew, movie keywords, descriptions etc. The app in background finds the most similar movies that matches with it and returns the top 5 match.
## song recommender section 
A song recommender system that finds the top five similar songs based on similariy of lyrics between them. 

## Tech used
Made use of python libaries such as sklearn and its cosine similarity function to find the relative similarity between all song and movies<br>
Used streamlit to make the web application. To apps movie and song recommender are put in one using a third .py app. <br>
For API calls made use of TMDB api and spotipy. <br>
To train the model used dataset from kaggle.<br>
Song dataset: https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset<br>
Movie dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata<br>
