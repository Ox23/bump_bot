import discord
import asyncio
from discord.ext import commands, tasks
import time

token = ""

client = commands.Bot("$", self_bot=True)

@client.event
async def on_connect():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    channel = client.get_channel()
    while True:
        await channel.send('!d bump')
        print(f'bumped')
        time.sleep(7230)

client.run(token, bot=False)