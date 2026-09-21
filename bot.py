import aiohttp
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


@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if "https://" in message.content.lower():
        print(f"[There is an add!]")
        print(f"User: {message.author} (ID: {message.author.id})")
        print(f"Channel: {message.channel.name}")
        print(f"About: {message.content}")

        try:
            await message.delete()
            await message.guild.ban(message.author, reason="Automated ban for sharing link")
            
            await message.channel.send(f"🚫 {message.author.mention} is automatically banned for sharing a link.")
        
        except discord.Forbidden:
            print("ERROR: I don't have permission to ban this user.")
        except discord.HTTPException as e:
            print(f"ERROR: Failed to ban user: {e}")


async def get_img(self):
        # PokeAPI üzerinden Pokémon görselini almak için asenkron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için API URL'si
        async with aiohttp.ClientSession() as session:  # HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtını alma
                    # Pokémon'un varsayılan görsel bağlantısını döndürme
                    return data['sprites']['front_default']
                else:
                    # İstek başarısız olursa varsayılan bir görsel/hata URL'si döndürür
                    return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"



@client.event
async def on_member_join(member):
    for channel in member.guild.text_channels:
        await channel.send(f" Welcome, {member.mention}!")


client.run(token)
