import discord
import asyncio
from redditAPI import redditMemes
import praw


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
    if message.author == client.user:
        return

    message.content = message.content.lower()

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.startswith("yo"):
        await message.channel.send("yo?")



#reddit
    if message.content.startswith("new memes"):
        memes = redditMemes("new")
        await message.channel.send(memes)
    if message.content.startswith("best memes"):
        memes = redditMemes("best")
        await message.channel.send(memes)

client.run('NzcwNTg2NTgwNzI5MjAwNjgw.X5furQ.smTytMUFagjAzbMuOpWrrIE_jag')
