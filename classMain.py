import discord
from message import getMessage
from redditAPI import Reddit
from moviesAPI import IMDBmovies
from musicAPI import spotify

client = discord.Client()


class Bot(discord.Client):
    async def on_ready(self):
         print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        
        if message.author == self.user:
            return
        
        else:
            mess = message.content
            split_mess = mess.split()


            if split_mess[0] == "doge":

                response = getMessage(mess)
                if response is not None:
                    await message.channel.send(response)

                elif mess == "doge show memes":
                    reddit = Reddit()
                    url = reddit.redditMemes()
                    await message.channel.send(url)

                elif mess.startswith("doge movie"):
                    lenth = len(split_mess)
                    if lenth <= 2:
                        await message.channel.send("Name the movie please")

                    else:
                        movie_name = []
                        for i in range(2, lenth):
                            movie_name += (split_mess[i])

                        movie_search = IMDBmovies(movie_name)
                        await message.channel.send(movie_search)

                elif mess.startswith("doge music latest"):
                    client = spotify()
                    await message.channel.send(client.latest_albums())





if __name__ == "__main__":
    bot = Bot()
    bot.run('NzcwNTg2NTgwNzI5MjAwNjgw.X5furQ.1X6RVwfkndymk3d-ZZKhzD1g0l4')
