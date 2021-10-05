#cogs/rank.py
import asyncio
from os import path
import discord
from discord.ext import commands
import random
import json

class Rank(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Rank Cog is Ready")
        
    @commands.command(name = "랭킹")
    async def _rank(self,ctx, args=None):
        with open("./data/score.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
            sort_data = sorted(data.items(), key = lambda x : x[1], reverse = True)

        if args == None:
            embed = discord.Embed(title='전체 랭킹',description="전체 퀴즈 랭킹입니다.", color = discord.Color.blue())

            for key, rank in enumerate(sort_data):
                embed.add_field(name = f"{key+1}. {rank[0]}",value = f"점수 : {rank[1]}점",inline = False)
                
        elif args != None:

            for key,rank in enumerate(sort_data):
                if args in rank:
                    embed = discord.Embed(title="개인 랭킹",description="개인 퀴즈 랭킹입니다.",color=discord.Color.blue())

                    embed.add_field(name= args,value=f"{rank[1]}점으로 {key+1}등 입니다",inline=False)
                    break
                else:
                    embed = discord.Embed(title="오류",description="잘못된 입력입니다. \n다시 입력하세요",color=discord.Color.red())
                    continue
                    
        await ctx.send(embed=embed)
    
def setup(client):
    client.add_cog(Rank(client))
