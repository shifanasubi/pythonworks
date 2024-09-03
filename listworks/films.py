movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]
#q1 total_number_of_movies

# movies_count=len(movies)
# print("movies_count",movies_count)


#q2 movies with genre Drama

# genre_filter=[m.get("title")for m in movies if "Drama" in m.get("genres")]
# print(genre_filter)

#q3 latest movie

# def get_year(mov):
    # return mov.get("year")
# latest_movie=max(movies,key=get_year)
# latest_moviess=[m.get("title")for m in movies if m.get("year")==latest_movie.get("year")]
# print(latest_moviess)

#q4 top movie (movie with higest rating)

def get_rating(mov):
    return mov.get("rating")
top_rating=max(movies,key=get_rating)
top_rating_movies= [m.get("title") for m in movies if m.get("rating")==top_rating.get("rating")]
# print(top_rating_movies)

#q5 movies with language malayalam
malayalam_movies=[m.get("title") for m in movies if m.get("language")=="Malayalam"]
# print(malayalam_movies)

#q6 movies released after year 2016
year_filter=[m.get("title")for m in movies if m.get("year")>2016]
# print(year_filter)

#q7 movie with lowest rating
def get_rating(mov):
    return mov.get("rating")
rating=min(movies,key=get_rating)
lowesr_rating=[m.get("title") for m in movies if m.get("rating")==rating.get("rating")]
# print(lowesr_rating)

#q8 malayalam movies with genere Action
action_movie=[m for m in movies if "Action" in m.get("genres") and "language"=="Malayalam"]
# print(action_movie)

# q9 movies releasd in same years
movie_dictionary={}
for m in movies:
    release_year=m.get("year")
    if release_year in movie_dictionary:
        movie_dictionary.get(release_year).append(m.get("title"))
    else:
        movie_dictionary[release_year]=[m.get("title")]
# print(movie_dictionary)

# q10 oldest movie
def get_year(mov):
    return mov.get("year")
oldest=min(movies,key=get_year)
oldest_movie=[m.get("title") for m in movies if m.get("year")==oldest.get("year")]
# print(oldest_movie)

# movie name with generes either Drama or Comedy

drama_or_comedy=[m.get("title") for m in movies if "Drama" in m.get("genres") or "comedy" in m.get("genres")]
print(drama_or_comedy)

# number of movies released in each year
year=[m.get("year") for m in movies]
year_count={y:year.count(y) for y in year}
# print(year_count)


# print all genres
# all_genres={g for m in movies for g in m.get("genres")}
# print(all_genres)

# action:2,drama:2
all_genres=[g for m in movies for g in m.get("genres")]
genre_count={g:all_genres.count(g) for g in all_genres}
# print(genre_count)

sorted_movies=(movies,key=lambda mov:mov.get("tutle"))
sorted_moviess=[m.get("title")for m in sorted_movies]
print(sorted_moviess)