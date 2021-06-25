from staticMessages import commonGreetings, getMessage
from moviesAPI import IMDBmovies
from musicAPI import spotify
from redditAPI import Reddit

def resp(mess):
    split_mess = mess.split()

    response = getMessage(input)

    if response is not None:
        return response

    elif mess == "doge show memes":
        reddit = Reddit()
        url = reddit.redditMemes()
        return url


    elif mess.startswith("doge movie"):
        lenth = len(split_mess)
        if lenth <= 2:

            return "Name the movie please"

        else:
            movie_list = []
            for i in range(2, lenth):
                movie_list.append(split_mess[i])

            movie_name = (" ".join(movie_list))
            

            movie_search = IMDBmovies(movie_name)

            return movie_search

    elif mess.startswith("doge music latest"):
        client = spotify()

        return client.latest_albums()

    else:
        return None
