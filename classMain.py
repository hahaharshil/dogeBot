import discord
from message import getMessage
client = discord.Client()


class Bot(discord.Client):

    async def on_ready(self):
        print(f'We have logged in as {client}')

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send('Hello!')
        if message.content.startswith("yo"):
            await message.channel.send("yo?")
        response = getMessage(message.content)
        if response is not None:
            await message.channel.send(response)


if __name__ == "__main__":
    bot = Bot()
    bot.run('NzcwNTg2NTgwNzI5MjAwNjgw.X5furQ.1X6RVwfkndymk3d-ZZKhzD1g0l4')
