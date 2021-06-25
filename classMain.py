import discord

from message import resp

client = discord.Client()


class Bot(discord.Client):
    async def on_ready(self):
         print(f'We have logged in as {self.user}')

    async def on_message(self, message):

        if message.author == self.user:
            return

        else:
            user_mess = message.content
            split_mess1 = user_mess.split()

            if split_mess1[0] == "doge":

                messages = await resp(user_mess)
                if messages is not None:
                    await message.channel.send(messages)







if __name__ == "__main__":
    bot = Bot()
    bot.run('NzcwNTg2NTgwNzI5MjAwNjgw.X5furQ.1X6RVwfkndymk3d-ZZKhzD1g0l4')
