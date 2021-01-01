import discord
from dotenv import load_dotenv
load_dotenv()
import os
import time


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!shroud '):
        time.sleep(10)
        await message.delete()

client.run(os.getenv('TOKEN'))