import discord
import asyncio
from inspireAPI import get_quote
import praw



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run('NzcwNTg2NTgwNzI5MjAwNjgw.X5furQ.loybiSIUwbxl13x1-mejkHDIv78')
