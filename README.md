## Movie Recommender System
#### This is a movie recommender system built using Python, Pandas, Numpy, Scikit-learn and Streamlit. It uses the TMDb dataset to recommend 5 similar movies based on the selected movie.


## Demo Video

https://github.com/NMurari7/movies_recommender_system/assets/70143030/5e546779-d61e-4213-8ed3-231221f88932



### Screenshots
<img width="586" alt="image" src="https://user-images.githubusercontent.com/70143030/208256984-814f9a86-5f02-4391-9bfe-1baf87af888a.png">
<img width="596" alt="image" src="https://user-images.githubusercontent.com/70143030/208257025-1edb6911-0d37-427a-bef0-2c14d5bc7d70.png">



### Installation
To install the required packages, run the following command:

pip install pandas numpy scikit-learn streamlit

Dataset
The dataset used for this project is the TMDb dataset. It contains information about movies, including their titles, genres, overviews, and other details. The dataset can be found at https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata.

### Usage
To run the application, simply run the following command in your terminal:

streamlit run app.py

This will start the application and open it in your default web browser. From there, you can select a movie from the dropdown menu, and the app will recommend 5 similar movies based on the cosine similarity of their descriptions and other details.

### Development
This application was developed using Python, Pandas, Numpy, Scikit-learn and Streamlit. 

### Credits
This project was developed by N Murari. It is based on the TMDb dataset, which was collected by TMDb and made available on Kaggle.
