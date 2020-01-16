import discord
import asyncio
import requests
from bs4 import BeautifulSoup
from datetime import datetime


TOKEN = "bmpzCA7dG7H16Avrhx77yqZQGI3kvjc5"
CHANNEL_ID = 666999245114572810

text_chat = discord.Object(id=CHANNEL_ID)
client = discord.Client()
r = requests.get('https://anime.eiga.com/program/')
soup = BeautifulSoup(r.text, 'html.parser')
title_text = soup.find_all('div',{'class':'seasonBoxImg'})

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    asyncio.ensure_future(greeting_gm())

async def greeting_gm():
    channel = client.get_channel(CHANNEL_ID)
    while True:
        now = datetime.now().strftime('%H:%M')
        weekno = datetime.now().strftime('%w')
        if now == '01:18' and weekno == '5':
            await channel.send(now+'です まもなく「推しが武道館いってくれたら死ぬ 」の時間です')
        await asyncio.sleep(60)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('今期アニメ'):
        #番組名を取り出して一行づつ
        text = ''
        channel = client.get_channel(CHANNEL_ID)
        for t in soup.find_all('div',{'class':'seasonBoxImg'}):
            text +=  t.get_text()+'\n'
        await message.channel.send('**今期のアニメ一覧**')
        await message.channel.send(text)
        #await message.channel.send('Hello!')

client.run(TOKEN)
