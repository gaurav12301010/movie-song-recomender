import streamlit as st

pages = {
    "Movies": [
        st.Page("app.py", title="Movie Recommender"),
    ],
    "Songs": [
        st.Page("app3.py", title="Song Recommender"),
    ],
}

pg = st.navigation(pages)
pg.run()