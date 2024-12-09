# MFG:598  Movie Recommendation System
 Class Project Files


Overview
This project is a Movie Recommendation System developed as part of the MFG 598 coursework. The system uses machine learning techniques and a variety of Python libraries to recommend movies based on user input. The application is designed as a Python-based web app and deploys a collaborative filtering approach to identify and suggest similar movies.

# Requirements

Libraries: Numpy, Pandas, Scikit-learn, and Streamlit.
Graphical User Interface: Web-based interface for user interaction.
Machine Learning: Implementation of similarity-based movie recommendation.
Dataset: TMDB 5000 Movies dataset sourced from Kaggle.
Processing Environment:
Data Preprocessing: Google Colab.
Web Application Development: PyCharm IDE.
Deployment: Streamlit.

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
