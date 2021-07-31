import praw



class Reddit:

    def __init__(self):
        #You will have to rejister you bot in reddit.com/prefs/apps and enter all the details.
        self.reddit = praw.Reddit(client_id="Your client id",
                                  client_secret="Your client secret",
                                  username="your username",
                                  password="",
                                  user_agent="user agent name")

    async def redditMemes(self):
        try:
            subreddit = self.reddit.subreddit("memes")
            new = await subreddit.new()

            for submission in new:
                return submission.url
        except Exception:
            pass
