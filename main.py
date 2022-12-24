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
# youtube_dl.utils.bug_reports_message = lambda: ''
#
# ytdl_format_options = {
#     'format': 'bestaudio/best',
#     'restrictfilenames': True,
#     'noplaylist': True,
#     'nocheckcertificate': True,
#     'ignoreerrors': False,
#     'logtostderr': False,
#     'quiet': True,
#     'no_warnings': True,
#     'default_search': 'auto',
#     'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
# }
#
# ffmpeg_options = {
#     'options': '-vn'
# }
#
# ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
#
# class YTDLSource(discord.PCMVolumeTransformer):
#     def __init__(self, source, *, data, volume=0.5):
#         super().__init__(source, volume)
#         self.data = data
#         self.title = data.get('title')
#         self.url = ""
#
#     @classmethod
#     async def from_url(cls, url, *, loop=None, stream=False):
#         loop = loop or asyncio.get_event_loop()
#         data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
#         if 'entries' in data:
#             # take first item from a playlist
#             data = data['entries'][0]
#         filename = data['title'] if stream else ytdl.prepare_filename(data)
#         return filename
@bot.slash_command(description="音楽を再生する。")
async def play(ctx: ApplicationContext, url):
    await ctx.respond("Connecting...")
    await ctx.user.voice.channel.connect()

    greeting = """
Created by Yuki.
/play [URL] で再生.
/leave で退出."""
    await ctx.send(embed=Embed(title="YukiMusic" ,description=greeting, colour=discord.Colour.dark_red()))



bot.run(TOKEN)