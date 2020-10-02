import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

client.run('NDA1ODkyMDExMTYyMzM3Mjgz.WmkuZA.0dkWXVxX6wISApWCLYd3-4EVZEM')