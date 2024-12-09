import pickle
import streamlit as st

# Function to recommend movies
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]  # Top 5 recommendations
        return recommended_movie_names
    except IndexError:
        st.error("Selected movie not found in the dataset.")
        return []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Streamlit app
st.header('Movie Recommender System')

# Load movies and similarity data
movies = pickle.load(open('./movie_list.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))

# Dropdown for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to display recommendations
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

    # Display recommendations
    if recommended_movie_names:
        st.write("Recommended Movies:")
        for name in recommended_movie_names:
            st.write(f"- {name}")
    else:
        st.error("No recommendations available.")
