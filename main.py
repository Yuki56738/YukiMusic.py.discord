import asyncio

import discord
from discord import *
import youtube_dl
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
intents = discord.Intents().all()

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user}")

@bot.slash_command(description="音楽を再生する。")
async def play(ctx: ApplicationContext, url):
    await ctx.respond("Connecting...")
    await ctx.user.voice.channel.connect()

    greeting = """
Created by Yuki.
/play [URL] で再生.
/leave で退出."""
    await ctx.send(embed=Embed(title="YukiMusic" ,description=greeting, colour=discord.Colour.dark_red()))

    #URLを取得
    filename = await YTDLSource.from_url(url)
    #再生する
    await play(discord.FFmpegPCMAudio(source=filename))
    await ctx.send(f"再生中: {filename}")


bot.run(TOKEN)