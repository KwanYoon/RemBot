import discord
from discord.ext import commands
import time
import praw
import urllib3

red = praw.Reddit(
     client_id="RlzWM0NK17wdOQ",
     client_secret="mBs-_oP_lK7IxTaGJlgtiWlkGStILw",
     user_agent="discord:RemBotv1.0:(By /u/rKeWdAiNt)"
 )

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print(red.read_only)

@bot.command()
async def add(ctx, num1: float, num2: float):
    await ctx.send(num1 + num2)

@bot.command()
async def sub(ctx, num1: float, num2: float):
    await ctx.send(num1 - num2)

@bot.command()
async def reddit(ctx, subr: str):
    for submission in red.subreddit(subr).top(limit=5):
        await ctx.send(submission.url)

bot.run('NDA1ODkyMDExMTYyMzM3Mjgz.WmkuZA.0dkWXVxX6wISApWCLYd3-4EVZEM')