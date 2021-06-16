import praw


def redditMemes(type):
    reddit = praw.Reddit(client_id = "zCoycm00P_3vKQ",
                         client_secret = "aHJeLn3Rof7lOq-r0rWdUUVKY6Y57Q",
                         username = "hahaharshil",
                         password = "",
                         user_agent = "sainika")



    subreddit = reddit.subreddit("memes")
    if type == "new":
        new = subreddit.new()

        for submission in new:
            return submission.url

    if type == "best":
        best = subreddit.hot()

        for submission in best:
            return submission.url

def cursedImages():
    reddit = praw.Reddit(client_id = "zCoycm00P_3vKQ",
                         client_secret = "aHJeLn3Rof7lOq-r0rWdUUVKY6Y57Q",
                         username = "hahaharshil",
                         password = "",
                         user_agent = "sainika")



    subreddit = reddit.subreddit("cursedimage")

    best = subreddit.hot()

    for submission in best:
        return submission.url
