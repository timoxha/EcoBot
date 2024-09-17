import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith('>help'):
        await message.channel.send("'>credits': никнейм создателя \n '>how_to_save': Подсказки, как можно сохранить природу")
    elif message.content.startswith('>how_to_save'):
        randomik = random.randint(1,8)
        if randomik == 1:
            await message.channel.send('Сортируй мусор в разные контейнеры!')
        elif randomik == 2:
            await message.channel.send('Меньше пользуйся пластиковыми тарелками, столовыми приборами и т. д.!')
        elif randomik == 3:
            await message.channel.send('Экономь электричество!')
        elif randomik == 4:
            await message.channel.send('Береги воду!')
        elif randomik == 5:
            await message.channel.send('Не разбрасывайся мусором!')
        elif randomik == 6:
            await message.channel.send('Употребляй натуральные продукты!')
        elif randomik == 7:
            await message.channel.send('Не покупай электрические машины!')
        elif randomik == 8:
            await message.channel.send('Покупай продукты, которые сделаны с любовью к природе (ЭКО и другие)')
    elif message.content.startswith('>credits'):
        await message.channel.send('Создатель: timoxha001')

client.run('My Token')
