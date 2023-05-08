import pickle
import streamlit as st
import requests
# import pandas as pd


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=450157a10c39720265595d4d414b12f1&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_desc = []
    recommended_movie_director = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_desc.append(movies_df.iloc[i[0]].overview)
        recommended_movie_director.append(movies_df.iloc[i[0]].director)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_desc, recommended_movie_director


st.header('Movie Recommender System')
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pickle.load(open('movie_list.pkl', 'rb'))
movies_df = pickle.load(open('movies_df.pkl', 'rb'))


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_desc, recommended_movie_director = recommend(selected_movie)
    join = lambda x: " ".join(x)
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.image(recommended_movie_posters[0])
    # with col2:
    #     st.text(recommended_movie_names[0])
    #     st.text(recommended_movie_desc[0])
    #     st.text(recommended_movie_director[0])
    #
    # col3, col4 = st.columns(2)
    # with col3:
    #     st.image(recommended_movie_posters[1])
    # with col4:
    #     st.text(recommended_movie_names[1])
    #     st.text(recommended_movie_desc[1])
    #     st.text(recommended_movie_director[1])

    # col1, col2 = st.columns([5,20])

    col1, col2= st.columns(2)
    with col1:
        st.image(recommended_movie_posters[0], width=250)


    with col2:
        st.subheader(recommended_movie_names[0])
        join = lambda x: " ".join(x)
        desc = join(recommended_movie_desc[0])
        st.write(desc)
        st.write("Directed by:- ",recommended_movie_director[0][0])

    col3, col4 = st.columns(2)
    with col3:
        st.image(recommended_movie_posters[1], width=250)

    with col4:
        st.subheader(recommended_movie_names[1])
        join = lambda x: " ".join(x)
        desc = join(recommended_movie_desc[1])
        st.write(desc)
        st.write("Directed by:- ", recommended_movie_director[1][0])

    col5, col6 = st.columns(2)
    with col5:
        st.image(recommended_movie_posters[2], width=250)

    with col6:
        st.subheader(recommended_movie_names[2])
        join = lambda x: " ".join(x)
        desc = join(recommended_movie_desc[2])
        st.write(desc)
        st.write("Directed by:- ", recommended_movie_director[2][0])

    col7, col8 = st.columns(2)
    with col7:
        st.image(recommended_movie_posters[3], width=250)

    with col8:
        st.subheader(recommended_movie_names[3])
        join = lambda x: " ".join(x)
        desc = join(recommended_movie_desc[3])
        st.write(desc)
        st.write("Directed by:- ", recommended_movie_director[3][0])

    col9, col10 = st.columns(2)
    with col9:
        st.image(recommended_movie_posters[4], width=250)

    with col10:
        st.subheader(recommended_movie_names[4])
        join = lambda x: " ".join(x)
        desc = join(recommended_movie_desc[4])
        st.write(desc)
        st.write("Directed by:- ", recommended_movie_director[4][0])

