import streamlit as st
import pandas as pd
import re

#Set page
st.set_page_config(
    page_title="IMDb Top 250 Movies App",
    page_icon="🍿",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
       'About': "# IMDb Top 250 Movies App. It helps you to make a choice!"
    }
 )


#Containers
header = st.container()
movie_title = st.container()
actor = st.container()
genre = st.container()
duration = st.container()
note = st.container()

#Cleaning operations 
movie_data = pd.read_csv('imdb_project/movie_crawl.csv')
movie_data["movie_runtime"]= movie_data["movie_runtime"].str.replace(",","").str.replace(" ","")
movie_data["genre"]= movie_data["genre"].str.replace(",",", ")
movie_data["actors"]= movie_data["actors"].str.replace(",",", ")
movie_data["country_of_origin"]= movie_data["country_of_origin"].str.replace(",",", ")
movie_data["orginal_language"]= movie_data["orginal_language"].str.replace(",",", ")
movie_data["original_title"]= movie_data["original_title"].fillna("-")
movie_data["original_title"]= movie_data["original_title"].str.replace("Original title:", "")
movie_data["public"]= movie_data["public"].fillna("-")
movie_data_clean = movie_data.copy()
movie_data_clean["movie_runtime"]= movie_data_clean["movie_runtime"].str.replace("minutes","").str.replace("hour","h").str.replace("hs","h")
movie_data_clean = movie_data_clean.rename(columns={
    "title": "Movie Title",
    "original_title": "Original Title",
    "movie_note": "Movie Rating",
    "genre": "Genre",
    "date_pub": "Release Date",
    "movie_runtime": "Movie Runtime",
    "public": "Public",
    "synopsis": "Synopsis",
    "actors": "Main Cast",
    "orginal_language": "Original Language",
    "country_of_origin": "Country of Origin"
})

#Duration
a= movie_data["movie_runtime"].str.replace(",","").str.replace(" ","")
hour= a.str.extract(r'(\d+)h')
minutes = a.str.extract(r'(\d+)m')
hour= hour.astype("float", errors='ignore')
minutes= minutes.astype("float", errors='ignore')
hour = hour[0].fillna(0.0)
minutes = minutes[0].fillna(0.0)
movie_duration = (hour * 60) + minutes
clone_data = movie_data_clean.copy()
clone_data["Duration"] = movie_duration

#Variables
movie_list = movie_data["title"]
actors_list = pd.unique(movie_data["actors"].str.split(",").explode("actors").sort_values())
movie_genre = pd.unique(movie_data["genre"].str.split(",").explode("genre"))

#Sidebar
home = st.sidebar.button("Home")
user_filter = st.sidebar.radio('Filter by: ', ('None','Movie', 'Actor', 'Genre', 'Runtime', 'Movie Rating'))


with header:
    if home:
        '# IMDb TOP 250 Movies of all time'
        st.dataframe(movie_data_clean)

if user_filter == 'None':
    '# IMDb TOP 250 Movies of all time'
    st.dataframe(movie_data_clean)

with movie_title:
    # user_text_input = st.text_input('What movie are you looking for?', value="The Big Lebowski", type="default", autocomplete= "on")
    # user_movie_select = st.selectbox('What movie are you looking for?', options= movie_list, index=120)
    if user_filter == 'Movie':
        '### Filter by Movie'
        user_movie_select = st.sidebar.selectbox('What movie are you looking for?', options= movie_list, index=120)
        df_movie_title = st.write(movie_data_clean[movie_data_clean["Movie Title"].str.contains(user_movie_select)], height= 300, width= 500)
        
with actor:
    # user_actor_select = st.selectbox('Select an Actor: ', options= actors_list, index=120)
    if user_filter == 'Actor':
        '### Filter by Actor'
        user_actor_select = st.sidebar.selectbox('Select an Actor: ', options= actors_list, index=120)
        df_actors = st.write(movie_data_clean[movie_data_clean["Main Cast"].str.contains(user_actor_select)], height= 300, width= 500)

with genre:
    # user_genre_select = st.selectbox('Select a Genre: ', options= movie_genre, index=4)
    if user_filter == 'Genre':
        '### Filter by Genre'
        user_genre_select = st.sidebar.selectbox('Select a Genre: ', options= movie_genre, index=4)
        df_movie_genre = st.write(movie_data_clean[movie_data_clean["Genre"].str.contains(user_genre_select)])

with duration:
    # user_duration_select = st.slider('Movie Runtime: ', min_value=40.0, max_value=350.0, value=121.0, step=1.0)
    if user_filter == 'Runtime':
        '### Filter by Runtime'
        user_duration_select = st.sidebar.slider('Movie Runtime: ', min_value=40.0, max_value=350.0, value=121.0, step=1.0)
        df_movie_duration = st.write(clone_data[clone_data["Duration"] == user_duration_select])

with note:
    # user_note_select = st.slider('Movie Rating: ', min_value=8.0, max_value=10.0, value=8.3, step=0.1)
    if user_filter == 'Movie Rating':
        '### Filter by Movie Rating'
        user_note_select = st.sidebar.slider('Movie Rating: ', min_value=8.0, max_value=10.0, value=8.3, step=0.1)
        df_movie_note = st.write(movie_data_clean[movie_data_clean["Movie Rating"] == user_note_select])




