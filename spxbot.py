#spx

import discord 
from discord.ext import commands
import asyncio
from asyncio import sleep
import time 

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print("Logged in as", client.user.name,".")
    await client.change_presence(activity=discord.Game(name='spam.'))

@client.command()
async def hi(ctx):
    await sleep(1)
    for _ in range(1000):
       await ctx.send("@everyone")
       await sleep(0)

@client.command()
async def test(ctx):
    await ctx.send("test verified.")

client.run("INSERT TOKEN IN BETWEEN THE QUOTES")
