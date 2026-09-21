import aiohttp
import discord
from discord.ext import commands
import random
from config import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Oyuncuların Pokémon'larını tutan sözlük
pokemons = {}

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

@bot.command()
async def pokemon_al(ctx):
    """Oyuncuya rastgele Dövüşçü veya Sihirbaz Pokémon verir."""
    poke_id = random.randint(1, 151)
    
    # Rastgele Sihirbaz veya Dövüşçü sınıfı seçimi
    if random.choice([True, False]):
        poke = Wizard(poke_id, ctx.author.name)
        sinif_adi = "🔮 Sihirbaz"
    else:
        poke = Fighter(poke_id, ctx.author.name)
        sinif_adi = "🥊 Dövüşçü"
        
    await poke.fetch_data()
    pokemons[ctx.author.id] = poke
    
    embed = discord.Embed(title=f"Yeni Pokémon Kartı! ({sinif_adi})", description=poke.info(), color=discord.Color.green())
    embed.set_image(url=poke.img_url)
    await ctx.send(embed=embed)

@bot.command()
async def savas(ctx, rakip: discord.Member):
    """Etiketlenen rakip ile savaş başlatır: !savas @kullanici"""
    if ctx.author.id not in pokemons or rakip.id not in pokemons:
        await ctx.send("❌ Savaşabilmek için iki tarafın da önce `!pokemon_al` yapması gerekir!")
        return

    saldiran_poke = pokemons[ctx.author.id]
    savunan_poke = pokemons[rakip.id]

    savas_sonucu = await saldiran_poke.attack(savunan_poke)
    await ctx.send(savas_sonucu)


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
