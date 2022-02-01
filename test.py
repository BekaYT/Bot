import discord
import asyncio
import os

client = discord.Client()

token = os.environ["TOKEN"]

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 실행되었습니다')
    game = discord.Game('최류탄유튜브 서버에서 활동중')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.guild == None:
    return
  
  if message.content.startswith("케엔아"):
    query = message.content.replace("케엔아", "").replace(' ', '').replace("!", "").replace("?", "")
    if query == "ㅎㅇ" or query == "안녕" or query == "하이":
      await message.channel.send("안녕하세요! :wave:")

    if query == "와":
      await message.channel.send("샌즈!!")

    if query == "최류탄":
      await message.channel.send("https://www.youtube.com/channel/UCrQ2mWFhtgSZjxytOe8h_4A <- 최류탄 채널 링크")

    if query == "끄투":
      await message.channel.send("https://kkutu.co.kr <- 끄투코리아 링크")

    if query == "끄투코리아":
      await message.channel.send("https://kkutu.co.kr <- 끄투코리아 링크")

    if query == "최류탄유튜브":
      await message.channel.send("https://www.youtube.com/channel/UCrQ2mWFhtgSZjxytOe8h_4A <- 최류탄 채널 링크")
    
    if query == "명령어":
        embed = discord.Embed(title="케엔봇 명령어 목록", color=0x18dccf)
        embed.add_field(name="케엔아 최류탄유튜브", value="최류탄님의 유튜브 링크를 보냅니다")
        embed.add_field(name="케엔아 끄투코리아", value="끄투코리아 게임 링크를 보냅니다")
        embed.add_field(name="케엔아 와", value="케엔봇이 샌즈!!라고 답합니다",inline=False)
        embed.set_footer(text="Bot Made By Hikapu (aka Kenote) ")
        await message.channel.send(embed=embed)
        
client.run(token)
