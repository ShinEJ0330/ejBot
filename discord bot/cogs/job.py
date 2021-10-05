#cogs/job.py
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class Job(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Job Cog is Ready")

    @commands.command(name ="취업")
    async def job(self, ctx, keyword = None, *args):
        if keyword == None:
            embed = discord.Embed(title='오류 발생',description='키워드를 입력해주세요',color=discord.Color.red())
            await ctx.send(embed = embed)

        else:
            keyword += " %s"%(' '.join(args))
            url = f"https://www.jobkorea.co.kr/Search/?stext={keyword}"
            
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.select("ul.clear > li.list-post")

            for item in data[:5]:
                title = item.select_one('a').get('title')
                category = item.select_one('div.post-list-info > a').get('title')
                career = item.select_one('span.exp').text
                background = item.select_one('span.edu').text
                area = item.select_one('span.loc.long').text
                deadline = item.select_one('span.date').text
                etc = item.select_one('p.etc').text
                
                embed = discord.Embed(title = title, description = category, color = discord.Color.blue())
                embed.add_field(name = '경력 및 학력' , value = career + ", " + background)
                embed.add_field(name = '지역' , value = area)
                embed.add_field(name = '마감기한' , value = deadline)
                embed.add_field(name = '기타' , value = etc)
                await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Job(client))
