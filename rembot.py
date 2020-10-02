import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.event
async def on_message(message):
    channel = message.channel
    if message.content.startswith('@405892011162337283'):
        await client.send.send_message(channel, 'hehe')

client.run('NDA1ODkyMDExMTYyMzM3Mjgz.WmkuZA.0dkWXVxX6wISApWCLYd3-4EVZEM')