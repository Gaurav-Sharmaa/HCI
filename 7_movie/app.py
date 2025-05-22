from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def load_movies():
    try:
        return pd.read_csv('movies.csv')
    except Exception as e:
        print(f"Error loading movies.csv: {e}")
        # Create a sample dataset if file is empty or missing
        data = {
            'title': ['The Avengers', 'Toy Story', 'The Godfather', 'Pulp Fiction', 'The Dark Knight', 'Jurassic Park', 
                     'Frozen', 'The Matrix', 'Titanic', 'Star Wars'],
            'genres': ['Action|Adventure|Sci-Fi', 'Animation|Adventure|Comedy', 'Crime|Drama', 'Crime|Drama', 
                      'Action|Crime|Drama', 'Adventure|Sci-Fi', 'Animation|Adventure|Comedy', 'Action|Sci-Fi', 
                      'Drama|Romance', 'Action|Adventure|Sci-Fi'],
            'age_rating': [13, 8, 18, 18, 13, 13, 8, 16, 13, 10],
            'language': ['English', 'English', 'English', 'English', 'English', 'English', 'English', 'English', 'English', 'English'],
            'popularity': [8.5, 8.3, 9.2, 8.9, 9.0, 8.1, 7.5, 8.7, 7.8, 8.6]
        }
        return pd.DataFrame(data)

def get_recommendations(age, likeness, genres, language):
    movies = load_movies()
    # Filter by age and language
    filtered_movies = movies[movies['age_rating'] <= age]
    if language:
        filtered_movies = filtered_movies[filtered_movies['language'].str.lower() == language.lower()]
    
    # Calculate scores
    user_genres = set(genres.split('|'))
    results = []
    for _, movie in filtered_movies.iterrows():
        movie_genres = set(movie['genres'].split('|'))
        genre_match = len(user_genres.intersection(movie_genres)) / max(len(user_genres), 1)
        score = (genre_match * 0.6) + (movie['popularity'] / 10 * 0.2) + (likeness / 10 * 0.2)
        if score > 0.2:  # Only include if there's some relevance
            results.append((movie['title'], score))
    
    # Sort by score and return top 5
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:5]

@app.route('/', methods=['GET', 'POST'])
def index():
    results = None
    if request.method == 'POST':
        try:
            age = int(request.form.get('age', 18))
            likeness = int(request.form.get('likeness', 5))
            genres = request.form.get('genres', '')
            language = request.form.get('language', 'English')
            results = get_recommendations(age, likeness, genres, language)
        except Exception as e:
            print(f"Error processing recommendation: {e}")
            results = []
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
