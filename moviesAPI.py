from imdb import IMDb


ia = IMDb()


def IMDBmovies(name):
    try:
        movies = ia.search_movie(name)
        title = (movies[0]["title"])
        year = (movies[0]["year"])

        id = (movies[0].movieID)

        movie = ia.get_movie(id)
        rating = movie.data["rating"]

        for x in movie['genres']:
            genre = x

        return f"""
    ...
    Title :{title}
    Release year : {year}
    IMDB Rating : {rating}
    Genre : {"/".join(movie["genres"])}

        """
    except IndexError:
        return("not a movie bruh...")
