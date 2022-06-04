import discord
import random
import string
from discord.ext import commands

client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    print('Discord Chatfilter plugin made by xDark_M#0201 is online now!')

with open("badwords.txt") as file:
    bad_words = file.read().splitlines()

with open("allowedwords.txt") as file:
    allowedwords = file.read().splitlines()

allowedID = [128263404422037504,]


@client.event
async def on_message(message):

    if message.author.id in allowedID:
        return

    msg = message.content
    for word in allowedwords:
        if word in msg:
            return    
    for bad_word in bad_words:
        if bad_word in message.content.lower().split(" "):
            await message.delete()
            return

client.run('TOKEN MOET HIER')