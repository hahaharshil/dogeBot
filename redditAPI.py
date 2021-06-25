import praw



class Reddit:

    def __init__(self):
        self.reddit = praw.Reddit(client_id="zCoycm00P_3vKQ",
                                  client_secret="aHJeLn3Rof7lOq-r0rWdUUVKY6Y57Q",
                                  username="hahaharshil",
                                  password="",
                                  user_agent="sainika")

    async def redditMemes(self):
        try:
            subreddit = self.reddit.subreddit("memes")
            new = await subreddit.new()

            for submission in new:
                return submission.url
        except Exception:
            pass
