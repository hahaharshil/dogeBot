from moviesAPI import IMDBmovies
from musicAPI import spotify
from redditAPI import Reddit
from staticMessages import getMessage


async def resp(mess):
    split_mess = mess.split()

    response = getMessage(input)

    if response is not None:
        return response

    elif mess == "doge show memes":
        reddit = Reddit()
        url = await reddit.redditMemes()
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
    elif mess.startswith("doge playlist"):
        client = spotify()
        return client.featured_playlists()

    else:
        return None
