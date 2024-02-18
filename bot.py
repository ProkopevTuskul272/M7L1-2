import discord
from discord.ext import commands
import os
from options import TOKEN
from cl_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def photo(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            image_name = attachment.filename
            if image_name.endswith('.jpg') or image_name.endswith('.jpeg') or image_name.endswith('.png'):
                await attachment.save(f'images/{image_name}')
                await ctx.send('я ничё не понимаю, дай минуту')
                msg = await ctx.send('я ничё не понимаю, дай минуту')
                class_name, percentage_probability = get_class(model_path='model/keras_model.h5', labels_path='model/labels.txt', image_path=f'images/{image_name}')
                await msg.delete()
                await ctx.send(f'на селфи {class_name.lower()} и я уверен на {percentage_probability}%')
                os.remove(f'images/{image_name}')
            else:
                await ctx.send('я хаваю только .jpg, .jpeg, .png файлы, другие не принимаю')
                return
    else:
        await ctx.send('гони фотку')

bot.run(TOKEN)