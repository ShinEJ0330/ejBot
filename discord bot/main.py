import discord
from discord.ext import commands
import os

def main():
    prefix = ''
    intents = discord.Intents.all()

    client = commands.Bot(command_prefix=prefix, intents = intents)

    @client.event
    async def on_member_join(member):
        if member.dm_channel:
            channel = member.dm_channel
        else:
            channel = await member.create_dm()
        name = member.name
        await channel.send(f"{name}님, 안녕하세요! \'설명'을 입력해주세요!")

    @client.command(name = "새로고침")
    async def _reload(ctx, extension):
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f"{extension}이 새로고침 되었어요!")
        
    for filename in os.listdir('./cogs'):
        if '.py' in filename:
            filename = filename.replace('.py','')
            client.load_extension(f"cogs.{filename}")

    with open('token.txt', 'r') as f:
        token = f.read()
        
    client.run(token)

if __name__ == '__main__':
    main()
