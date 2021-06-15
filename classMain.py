import discord

client = discord.Client()


class Bot(discord.Client):

    async def on_ready(self):
        print(f'We have logged in as {client}')

    async def on_message(self,message):
        if message.author == client.user:
            return

        if message.content.startswith('hello'):
            await message.channel.send('Hello!')
        if message.content.startswith("yo"):
            await message.channel.send("yo?")


if __name__ == "__main__":
    bot = Bot()
    bot.run('ODU0MzE1MTY0Mjk0NTc4MjE2.YMiI_w.IELpy5woI2pSYMjxvchssZJclqI')
