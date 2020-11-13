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
async def reddit(ctx, subr: str, toptype: str, num: int):
    if num > 10 or num < 1:
        await ctx.send("Number has to be 1 ~ 10!")
    elif (toptype != "hot" and toptype != "new" and toptype != "top"):
        await ctx.send("The input has to be \"top\", \"new\", or \"hot\"!")
    elif (toptype == "top"):
        for submission in red.subreddit(subr).top(limit=num):
            embedVar = discord.Embed(title="Title", description=submission.title, color=0xadd8e6)
            embedVar.add_field(name="URL", value=submission.url, inline=False)
            embedVar.set_image(url=submission.url)
            await ctx.send(embed=embedVar)
    elif (toptype == "new"):
        for submission in red.subreddit(subr).new(limit=num):
            embedVar = discord.Embed(title="Title", description=submission.title, color=0xadd8e6)
            embedVar.add_field(name="URL", value=submission.url, inline=False)
            embedVar.set_image(url=submission.url)
            await ctx.send(embed=embedVar)
    elif (toptype == "hot"):
        for submission in red.subreddit(subr).hot(limit=num):
            embedVar = discord.Embed(title="Title", description=submission.title, color=0xadd8e6)
            embedVar.add_field(name="URL", value=submission.url, inline=False)
            embedVar.set_image(url=submission.url)
            await ctx.send(embed=embedVar)
    else:
        await ctx.send("Input is \".reddit subreddit type(top, new, hot) number\"")

bot.run('NDA1ODkyMDExMTYyMzM3Mjgz.WmkuZA.0dkWXVxX6wISApWCLYd3-4EVZEM')