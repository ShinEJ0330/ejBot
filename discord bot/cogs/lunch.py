#cogs/lunch.py
import discord
from discord.ext import commands
import json
import random

class Lunch(commands.Cog):
    def __init__(self,client):
        self.client = client
        #데이터 불러오기
        with open("./data/lunch.json",'r',encoding='utf-8') as f:
            self.lunchDict = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lunch Cog is Ready")

    @commands.command(name = '점심추천')
    async def _lunch(self, ctx, arg = None):
        if arg == None:
            categories = list(self.lunchDict.keys())
            category = random.choice(categories)
            lunch = random.choice(self.lunchDict[category])
            await ctx.send(f"오늘 점심은 ({category}){lunch} 어떠세요?")
        else:
            category = arg
            lunch = random.choice(self.lunchDict[category])
            await ctx.send(f"오늘 점심은 {lunch} 어떠세요?")

def setup(client):
    client.add_cog(Lunch(client))
