import streamlit as st
import pickle
import pandas as pd
import requests

# -------------------
# 1. Helper function to fetch poster from TMDB
# -------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=34b2f5bd7bfe76ae271a87e20b79f73d&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster"

# -------------------
# 2. Recommendation function
# -------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# -------------------
# 3. Load data (movies + similarity matrix)
# -------------------
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))

# -------------------
# 4. Streamlit UI
# -------------------
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Choose a movie you like:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])
