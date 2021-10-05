#cogs/ejBot.py
import discord
from discord.ext import commands

class EJBot(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ejBot Cog is Ready")
        
    @commands.command(name = "설명")
    async def embed(self, ctx):
        embed = discord.Embed(
            title = "이제이봇 설명",
            description = "원하는 기능을 입력하세요!",
            color = discord.Color.blue())
        embed.add_field(name="코로나", value="코로나바이러스 국내 현황을 알려줍니다.", inline=False)
        embed.add_field(name="점심추천", value="한식, 양식, 중식, 일식을 입력하면 그 중에서만 추천 가능합니다.", inline=False )
        embed.add_field(name="맛집", value="원하는 메뉴나 위치를 입력하시면 맛집을 찾아줍니다.", inline=False)
        embed.add_field(name="퀴즈", value="10초안에 정답을 입력하세요.", inline=False)
        embed.add_field(name="퀴즈랭킹", value="원하는 이름을 입력하시면 개인 점수 확인도 가능합니다.", inline=False)
        embed.add_field(name="음악재생", value="듣고 싶은 곡이나 가수를 입력하면 노래를 들을 수 있습니다. \n'일시정지', '다시시작', '음악종료'를 입력하면 원하는 기능을 실행 가능합니다.", inline=False)
        embed.add_field(name="취직", value="원하는 직무를 입력하세요.", inline=False)

        await ctx.send(embed = embed)
        
    @commands.command(name = "새로고침")
    async def _reload(ctx, extension):
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension}이 새로고침 되었어요!")

def setup(client):
    client.add_cog(EJBot(client))
