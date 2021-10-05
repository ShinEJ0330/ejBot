#cogs/music.py
import discord
from discord import embeds
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import command
from youtube_dl import YoutubeDL
from youtube_dl.postprocessor import ffmpeg
from .module.youtube import getUrl

class Music(commands.Cog):
    def __init__(self, client):
        option={
            'format':'bestaudio/best',
            'noplaylist':True,
        }
        self.client = client
        self.DL=YoutubeDL(option)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog is Ready")
    
    @commands.command(name="음악재생")
    #async def play_music(self, ctx, url):
    async def play_music(self, ctx, *keywords):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                embed=discord.Embed(title="오류 발생", description="음성 채널에 들어간 후 명령어를 사용해 주세요!", Color=discord.Color.red())
                await ctx.send(embed=embed)
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        
        keyword = ' '.join(keywords)
        url = getUrl(keyword)
        await ctx.send(url)
        embed=discord.Embed(title="음악 재생", description="음악 재생을 준비하고있어요. 잠시만 기다려주세요.", Color=discord.Color.blue())
        await ctx.send(embed=embed)

        data = self.DL.extract_info(url, download= False)
        link = data['url']
        title = data['title']

        ffmpeg_options={
            'options':'-vn',
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
        }
        player = discord.FFmpegPCMAudio(link, **ffmpeg_options, executable="C:/ffmpeg/bin/ffmpeg")
        ctx.voice_client.play(player)

        embed=discord.Embed(title="음악 재생", description=f"{title} 재생을 시작할게요!", Color=discord.Color.blue())
        await ctx.send(embed=embed)
    
    @commands.command(name="음악종료")
    async def quit_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_connected():
            await voice.disconnect()
            embed = discord.Embed(title=' ', description = "음악 재생을 종료합니다.", color= discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command(name="일시정지")
    async def stop_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_playing:
            voice.pause()
            embed = discord.Embed(title=' ', description = "음악 재생을 일시정지합니다.", color= discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command(name="다시시작")
    async def replay_music(self, ctx):
        voice = ctx.voice_client
        if voice.is_paused:
            voice.resume()
            embed = discord.Embed(title=' ', description = "음악 재생을 다시 시작합니다.", color= discord.Color.red())
            await ctx.send(embed=embed)           
def setup(client):
    client.add_cog(Music(client))
