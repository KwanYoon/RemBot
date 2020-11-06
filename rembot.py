import discord
from discord.ext import commands
import time
import praw
import urllib3

reddit = praw.Reddit(
     client_id="my client id",
     client_secret="my client secret",
     user_agent="my user agent"
 )

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def add(ctx, num1: float, num2: float):
    await ctx.send(num1 + num2)

@bot.command()
async def sub(ctx, num1: float, num2: float):
    await ctx.send(num1 - num2)

@bot.command()
async def reddit(ctx, subreddit: str):
    await ctx.send(reddit.subreddit(subreddit))

bot.run('NDA1ODkyMDExMTYyMzM3Mjgz.WmkuZA.0dkWXVxX6wISApWCLYd3-4EVZEM')