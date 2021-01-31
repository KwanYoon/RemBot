import discord
from discord.ext import commands
import tokens
import time
import praw
import urllib3


red = praw.Reddit(
     client_id=tokens.cid,
     client_secret=tokens.csecret,
     user_agent="discord:RemBotv1.0:(By /u/rKeWdAiNt)"
 )

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print(red.read_only)

@client.command()
async def add(ctx, num1: float, num2: float):
    await ctx.send(num1 + num2)

@client.command()
async def sub(ctx, num1: float, num2: float):
    await ctx.send(num1 - num2)

@client.command()
async def add(ctx, num1: float, num2: float):
    await ctx.sent (num1 * num2)

@client.command()
async def reddit(ctx, subr: str, toptype: str, num: int):
    if num > 10 or num < 1:
        await ctx.send("Number has to be 1 ~ 10!")
    elif (toptype != "hot" and toptype != "new" and toptype != "top"):
        await ctx.send("The input has to be \"top\", \"new\", or \"hot\"!")
    elif (toptype == "top"):
        for submission in red.subreddit(subr).top(limit=num):
            embedVar = discord.Embed(title="Title", description=submission.title, color=0xadd8e6)
            embedVar.add_field(name="URL", value="[Submission Link](https://reddit.com"+submission.permalink+")", inline=False)
            embedVar.set_image(url=submission.url)
            await ctx.send(embed=embedVar)
    elif (toptype == "new"):
        for submission in red.subreddit(subr).new(limit=num):
            embedVar = discord.Embed(title="Title", description=submission.title, color=0xadd8e6)
            embedVar.add_field(name="URL", value="[Submission Link](https://reddit.com"+submission.permalink+")", inline=False)
            embedVar.set_image(url=submission.url)
            await ctx.send(embed=embedVar)
    elif (toptype == "hot"):
        for submission in red.subreddit(subr).hot(limit=num):
            embedVar = discord.Embed(title="Title", description=submission.title, color=0xadd8e6)
            embedVar.add_field(name="URL", value="[Submission Link](https://reddit.com"+submission.permalink+")", inline=False)
            embedVar.set_image(url=submission.url)
            await ctx.send(embed=embedVar)
    else:
        await ctx.send("Input is \".reddit subreddit type(top, new, hot) number\"")

@client.event
async def on_message(message):
    await message.delete()


client.run(tokens.bot_token)