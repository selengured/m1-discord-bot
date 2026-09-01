import discord
from discord.ext import commands
import random
from config import token


class Car:
    def __init__(self, brand: str, color: str):
        self.brand = brand
        self.color = color

    def info(self) -> str:
        return f"🚗 **Car knowledge:** {self.color.capitalize()} colored **{self.brand.capitalize()}** produced!"


intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'Log in: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.attachments:
        for attachment in message.attachments:
            if attachment.content_type and attachment.content_type.startswith('image/'):
                await message.channel.send('Amazing! 📸')

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)

@client.command()
async def about(ctx):
    await ctx.send('This is bot that was made by .py library!')

@client.command()
async def choose(ctx, *choices: str):
    if not choices:
        await ctx.send('Please provide some options. Example: `!choose apple banana`')
        return
    await ctx.send(f'My choice: **{random.choice(choices)}** 🎯')


@client.command()
async def car(ctx, brand: str = None, color: str = None):
    if not brand or not color:
        await ctx.send("Please specify both brand and color! Example: `!car BMW red`")
        return

    my_car = Car(brand=brand, color=color)
    await ctx.send(my_car.info())


client.run(token)
