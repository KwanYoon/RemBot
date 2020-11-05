import discord
from discord.ext import commands

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

bot.run('NDA1ODkyMDExMTYyMzM3Mjgz.WmkuZA.0dkWXVxX6wISApWCLYd3-4EVZEM')