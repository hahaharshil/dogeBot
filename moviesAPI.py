from re import I
from imdb import IMDb
from imdb.utils import analyze_title
ia = IMDb()

def IMDBmoviesi(name):
    movies = ia.search_movie(name)
    title = (movies[0]["title"])
    year = (movies[0]["year"])
    id = (movies[0].movieID)
    
    print(analyze_title(title))


    # return title, year, id 


IMDBmoviesi("Race 3") 