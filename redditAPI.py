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
    return best.url
