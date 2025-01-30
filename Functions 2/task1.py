def is_high_rated(movie):
    return movie["imdb"] > 5.5

def filter_high_rated_movies(movies):
    return [movie for movie in movies if is_high_rated(movie)]

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]

def average_imdb_score(movies):
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

def average_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"}
]

print("1. Is 'Hitman' high rated?", is_high_rated(movies[1]))
print("2. Movies with IMDB score above 5.5:", filter_high_rated_movies(movies))
print("3. Movies in category 'Action':", movies_by_category(movies, "Action"))
print("4. Average IMDB score of all movies:", average_imdb_score(movies))
print("5. Average IMDB score for category 'Thriller':", average_imdb_score_by_category(movies, "Thriller"))