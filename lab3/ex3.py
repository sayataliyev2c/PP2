def is_above_5_5(movie):
    """
    Function to check if a movie's IMDB score is above 5.5
    """
    return movie["imdb"] > 5.5

def above_5_5_movies(movies):
    """
    Function to return a sublist of movies with an IMDB score above 5.5
    """
    return [movie for movie in movies if is_above_5_5(movie)]

def movies_in_category(movies, category):
    """
    Function to return movies under a specific category
    """
    return [movie for movie in movies if movie["category"] == category]

def average_imdb_score(movies):
    """
    Function to compute the average IMDB score of a list of movies
    """
    if not movies:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

def average_imdb_score_by_category(movies, category):
    """
    Function to compute the average IMDB score of movies under a specific category
    """
    category_movies = movies_in_category(movies, category)
    return average_imdb_score(category_movies)

# Test the functions
print(is_above_5_5(movies[0]))  # Output: True
print(above_5_5_movies(movies))  # Output: List of movies with IMDB score above 5.5
print(movies_in_category(movies, "Romance"))  # Output: List of romance movies
print(average_imdb_score(movies))  # Output: Average IMDB score of all movies
print(average_imdb_score_by_category(movies, "Romance"))  # Output: Average IMDB score of romance movies