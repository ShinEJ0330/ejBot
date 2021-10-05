#cogs/example.py
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("example Cog is Ready")

    @commands.command(name = "ping")
    async def _ping(self, ctx):
        await ctx.send('pong!')

    @commands.command(name = '시작')
    async def _name(self, ctx):
        name = ctx.message.author.name
        await ctx.send(f"반갑습니다. {name}님")

def setup(client):
    client.add_cog(Example(client))
