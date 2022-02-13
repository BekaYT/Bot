import discord
import asyncio
import random
import youtube_dl
import os

client = discord.Client()

intents = discord.Intents().all()

token = os.environ['TOKEN']

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 실행되었습니다')
    game = discord.Game('최적화30초동안')
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
      await message.channel.send("죄송합니다 ㅠㅠ 현재는 케엔봇이 업데이트중입니다 ㅠㅠ\n사유 : Railway 호스팅이 서버점검중...약 30분예상")

    if query == "와":
        await message.channel.send("샌즈!!")

    if query == "최류탄":
        await message.channel.send("https://www.youtube.com/channel/UCrQ2mWFhtgSZjxytOe8h_4A <- 최류탄 채널 링크")

    if query == "끄투코리아":
        await message.channel.send("https://kkutu.co.kr <- 끄투코리아 링크")

    if query == "최류탄유튜브":
        await message.channel.send("https://www.youtube.com/channel/UCrQ2mWFhtgSZjxytOe8h_4A <- 최류탄 채널 링크")

    if query == "명령어":
        embed = discord.Embed(title="케엔봇 명령어 목록", color=0x18dccf)
        embed.add_field(name="케엔아 최류탄유튜브", value="최류탄님의 유튜브 링크를 보냅니다",inline=False)
        embed.add_field(name="케엔아 끄투코리아", value="끄투코리아 게임 링크를 보냅니다",inline=False)
        embed.add_field(name="케엔아 와", value="케엔봇이 샌즈!!라고 답합니다",inline=False)
        embed.add_field(name="케엔아 랜덤음악", value="아무 NCS음악을 랜덤으로 보냅니다.",inline=False)
        embed.set_footer(text="Bot Made By Hikapu (aka Kenote) ")
        await message.channel.send(embed=embed)
         

    if query == "랜덤음악NCS":
        embed = discord.Embed(title="랜덤음악(NCS)", color=0x18dccf)
        music = random.choice([
          {'name': 'RetroVision - Puzzle [NCS Release]', 'link': 'https://www.youtube.com/watch?v=TN_8D-79BZg'},
          {'name': 'Janji - Heroes Tonight [NCS Release]', 'link': 'https://www.youtube.com/watch?v=3nQNiWdeH2Q'},
          {'name': 'DEAF KEV - Invincible [NCS Release]', 'link': 'https://www.youtube.com/watch?v=J2X5mJ3HDYE'},
          {'name': 'Cartoon - On & On [NCS Release]', 'link': 'https://www.youtube.com/watch?v=K4DyBUG242c'},
          {'name': 'Disfigure - Blank [NCS Release]', 'link': 'https://www.youtube.com/watch?v=p7ZsBPK656s'},
          {'name': 'Different Heaven & EH!DE - My Heart [NCS Release]', 'link': 'https://www.youtube.com/watch?v=jK2aIUmmdP4'},
          {'name': 'Elektronomia - Sky High [NCS Release]', 'link': 'https://www.youtube.com/watch?v=TW9d8vYrVFQ'},
          {'name': 'Warriyo - Mortals (feat. Laura Brehm) [NCS Release]', 'link': 'https://www.youtube.com/watch?v=yJg-Y5byMMw'},
          {'name': 'Cartoon - Why We Lose (feat. Coleman Trapp) [NCS Release]', 'link': 'https://www.youtube.com/watch?v=zyXmsVwZqX4'},
          {'name': 'Lost Sky - Fearless pt.II (feat. Chris Linton) [NCS Release]', 'link': 'https://www.youtube.com/watch?v=S19UcWdOA-I'},
          {'name': 'Spektrem - Shine [NCS Release]', 'link': 'https://www.youtube.com/watch?v=n4tK7LYFxI0'},
        ])
        embed.add_field(name=f"Music : {music['name']}", value=music['link'])
        embed.set_footer(text="⏏️ 위 링크 클릭시 노래재생 ⏏️\nBot Made By Hikapu (aka Kenote)")
        await message.channel.send(embed=embed)
    
    if query == "최신업데이트":
        embed = discord.Embed(title="최신업데이트 목록", color=0x18dccf)
        embed.add_field(name="'케엔아 랜덤음악NCS' 추가", value="케엔아 랜덤음악NCS 명령어를 쓰게되면 NCS노래중에 랜덤으로 나옵니다.\n2022-02-04 AM 11:42",inline=False)
        embed.add_field(name="'케엔아 출첵' 추가", value="출석체크가 됩니다.\n2022-02-04 PM 8:31",inline=False)
        embed.set_footer(text="Bot Made By Hikapu (aka Kenote) ")
        await message.channel.send(embed=embed)
    
    if query == "출첵":
        await message.channel.send(f'{message.author.mention}님 2022-02-13일 출석체크 완료되었습니다')
    
    
    if query == "VC입장":
        await message.author.voice.channel.connect()
        await message.channel.send("약2초후 보이스채널에 입장합니다.")

    if query == "VC퇴장":
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc

        await voice.disconnect()
        await message.channel.send("약2초후 보이스채널에 퇴장합니다.")
    
    if query.startswith('VC노래재생'):
         for vc in client.voice_clients:
             #f vc.guild == message.guild:
                 voice = vc

        #url = query.replace('VC노래재생')
        #option = {
           # 'outtmpl'_: "file/"+ url.split('=')[1] + ".mp3"
        #}
        
client.run(token)
