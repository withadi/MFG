# MFG:598  Movie Recommendation System
 Class Project Files


Overview
This project is a Movie Recommendation System developed as part of the MFG 598 coursework. The system uses machine learning techniques and a variety of Python libraries to recommend movies based on user input. The application is designed as a Python-based web app and deploys a collaborative filtering approach to identify and suggest similar movies.

# Requirements

1. Libraries: Numpy, Pandas, Scikit-learn, and Streamlit.
2. Graphical User Interface: Web-based interface for user interaction.
3. Machine Learning: Implementation of similarity-based movie recommendation.
4. Dataset: TMDB 5000 Movies dataset sourced from Kaggle.
5. Processing Environment:
a. Data Preprocessing: Google Colab.
b. Web Application Development: PyCharm IDE.
c. Deployment: Streamlit.

# Methodology
Data Preprocessing:

1. Loaded and cleaned the dataset using Pandas.
2. Extracted features such as genres, keywords, and cast for content-based filtering.
3. Transformed text data into numerical form using techniques like tokenization and TF-IDF vectorization.

Machine Learning:

Calculated cosine similarity between movie vectors using Scikit-learn.
Stored similarity metrics for quick reference during recommendations.
Web App Development:

Created a Streamlit app with a simple and interactive interface.
Integrated TMDB API for fetching movie posters.
Deployment:

Deployed the application locally using Streamlit for live recommendations.
