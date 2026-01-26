# recommender.py
# Sample recommender with intentional error for testing AI CI Agent

import pandas as pd

# Intentional typo in function name
def load_dtaa():
    data = {
        "user": ["Alice", "Bob", "Charlie"],
        "movie": ["Inception", "Titanic", "Matrix"],
        "rating": [5, 4, 5]
    }
    return pd.DataFrame(data)

def recommend_top_movies():
    # This line will cause an error (typo function call)
    df = load_data()  
    top_movies = df.groupby("movie")["rating"].mean().sort_values(ascending=False)
    print(top_movies)

if __name__ == "__main__":
    recommend_top_movies()
