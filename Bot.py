import discord
import config

from discord.ext import commands
bot = commands.Bot(command_prefix=config.Prefix)

client = discord.Client()


@client.event
async def on_ready():
    import random


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!Guess"):
        await message.channel.send("Guess a number between 1 and 10.")

client.run(config.Token)
