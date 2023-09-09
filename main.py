import discord
import random
from bot_log import *
from bot_token import ayarlar
import asyncio
emoji_list = ["🐒", "🤡 ", "😄", "🦋 ", "👊 ", "✍️ ", "👍 ", "👎", "🗿 ", "❄️ ", "🤓 ", "❤️ "]
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$emoji'):
         await message.channel.send(random.choice(emoji_list))
    elif message.content.startswith('$guess'):
        await guess_number(message)
    elif message.content.startswith('$help'):
        await message.channel.send('''
Bot Komutları:
- $hello: Size Merhaba olarak geri döner.
- $bye: Emoji yollar.
- $pass: Rastgele bir şifre oluşturur.
- $emoji: Rastgele bir emoji yollar.
- $guess: Bot bir sayı tutar ve siz tahmin etmeye çalışırınız.
- $help: Bütün komutları açıklamalarıyla birlikte listeler.
''')
    else:
        await message.channel.send(message.content)

async def guess_number(message):
    if message.content == '$guess':
        await message.channel.send('Guess a number between 1 and 10.')

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        answer = random.randint(1, 10)

        try:
            guess = await client.wait_for('message', check=is_correct, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send(f'Sorry, you took too long it was {answer}.')

        if int(guess.content) == answer:
            await message.channel.send('You are right!')
        else:
            await message.channel.send(f'Oops. It is actually {answer}')

client.run(ayarlar["TOKEN"])

