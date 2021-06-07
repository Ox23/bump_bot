import discord
import asyncio
from discord.ext import commands, tasks
import time

token = ""#your account token here

client = commands.Bot("$", self_bot=True)

@client.event
async def on_connect():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    channel = client.get_channel()#your channel id here
    while True:
        await channel.send('!d bump')
        print(f'bumped')
        await asyncio.sleep(9000)

client.run(token, bot=False)
