import discord
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

client.run('Nzk0NTc2MDUwMzg5Nzc4NDMy.X-80nA.4Ke-_h8BVqUfs4p1t99pJYu2hyA')