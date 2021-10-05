#cogs/corona.py
import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class Corona(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Corona Cog is Ready")

    @commands.command(name ="코로나")
    async def corona(self, ctx, *args):
        response = requests.get("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=")
        soup = BeautifulSoup(response.text, 'html.parser')
        date = soup.select_one("h5.s_title_in3 > span.t_date").text
        patient, released, isolation, dead = soup.select("div.caseTable > div")
        patient_acc = patient.select_one("dd.ca_value").text
        patient_today =  patient.select_one("p.inner_value").text
        released = released.select("dd.ca_value")
        released_acc, released_today = released[0].text, released[1].text.replace('\n', '')
        isolation = isolation.select("dd.ca_value")
        isolation_acc, isolation_today = isolation[0].text, isolation[1].text.replace('\n', '')
        dead = dead.select("dd.ca_value")
        dead_acc, dead_today = dead[0].text, dead[1].text.replace('\n', '')

        embed = discord.Embed(title = "코로나바이러스 국내 발생 현황("+date+")", description = "코로나바이러스 국내 발생 현황입니다.", color = discord.Color.blue())
        embed.add_field(name = '확진환자' , value = "누적:"+patient_acc+"\n전일대비:"+patient_today)
        embed.add_field(name = '격리해제' , value = "누적:"+released_acc+"\n전일대비:"+released_today)
        embed.add_field(name = '격리중' , value = "누적:"+isolation_acc+"\n전일대비:"+isolation_today)
        embed.add_field(name = '사망' , value = "누적:"+dead_acc+"\n전일대비:"+dead_today)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Corona(client))
