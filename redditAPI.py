import praw
import random


def redditMemes():
    reddit = praw.Reddit(client_id="zCoycm00P_3vKQ",
                         client_secret="aHJeLn3Rof7lOq-r0rWdUUVKY6Y57Q",
                         username="hahaharshil",
                         password="",
                         user_agent="sainika")

    subreddit = reddit.subreddit("memes")
    new = subreddit.new()

    for submission in new:
        print(submission.url)
        return submission.url

    # if type == "best":
    #     best = subreddit.hot(limit=65)
    #     best = list(best)
    #     random_num = random.randint(0, len(best) - 1)
    #     return best[random_num].url


def cursedImages():
    reddit = praw.Reddit(client_id="zCoycm00P_3vKQ",
                         client_secret="aHJeLn3Rof7lOq-r0rWdUUVKY6Y57Q",
                         username="hahaharshil",
                         password="",
                         user_agent="sainika")

    subreddit = reddit.subreddit("cursedcomments")

    best = subreddit.hot()

    for submission in best:
        return submission.url
<<<<<<< HEAD
    return best.url


=======
>>>>>>> 44dcb6f3fff928629135ebb98d253452cb12531e
