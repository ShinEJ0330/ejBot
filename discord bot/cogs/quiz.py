#cogs/Quiz.py
import asyncio
from os import path
import discord
from discord.ext import commands
import csv
import random

class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.quizDict = {}
        with open("./data/quiz.csv", 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                self.quizDict[row[0]] = row[1]

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Quiz Cog is Ready")

    @commands.command(name ="퀴즈")
    async def quiz(self, ctx):
        problemList = list(self.quizDict.keys())
        problem = random.choice(problemList)
        answer = self.quizDict[problem]
        embed = discord.Embed(title = '퀴즈', description = problem, color = discord.Color.blue())
        await ctx.send(embed=embed)

        def checkAnswer(message):
            if message.channel == ctx.channel and answer in message.content:
                return True
            else:
                return False
        try:
            message = await self.client.wait_for("message", timeout = 10.0, check = checkAnswer)
            name = message.author.name
            embed = discord.Embed(title = '', description = f'{name} 님, 정답이에요 !', color = discord.Color.blue())
            await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            embed = discord.Embed(title = '', description = f'땡! 시간초과입니다~ 정답은 {answer}이에요!', color = discord.Color.red())
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Quiz(client))
