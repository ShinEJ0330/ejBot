#cogs/restaurant.py
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class Restaurant(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Restaurant Cog is Ready")
        
    @commands.command(name ="맛집")
    async def restaurant(self, ctx, keyword = None, *args):
        if keyword == None:
            embed = discord.Embed(title='오류 발생',description='키워드를 입력해주세요',color=discord.Color.red())
            await ctx.send(embed = embed)

        else:
            keyword += " %s"%(' '.join(args))
            url = f"https://www.mangoplate.com/search/{keyword}"

            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers)

            soup = BeautifulSoup(response.text, 'html.parser')
            data = soup.select("li.server_render_search_result_item > div.list-restaurant-item")
            
            for item in data[:5]:
                thumbnail = item.select_one('img').get('data-original')
                link = item.select_one('a').get('href')
                title = item.select_one('h2.title').text.replace('\n', '')
                rating =item.select_one('strong.search_point').text
                category = item.select_one('p.etc').text
                view = item.select_one('span.view_count').text
                review = item.select_one('span.review_count').text
                
                embed = discord.Embed(title = title, description = category, color = discord.Color.blue())
                embed.set_thumbnail(url = thumbnail)
                embed.add_field(name = '평점' , value = rating)
                embed.add_field(name = '조회수' , value = view)
                embed.add_field(name = '리뷰수' , value = review)
                embed.add_field(name = '링크' , value = "https://www.mangoplate.com"+link, inline=False)
                await ctx.send(embed = embed)
 

def setup(client):
    client.add_cog(Restaurant(client))
