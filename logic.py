import aiohttp
import random

class Pokemon:
    def __init__(self, pokemon_number, pokemon_trainer):
        self.pokemon_number = pokemon_number
        self.pokemon_trainer = pokemon_trainer
        self.name = None
        self.img_url = None
        
        # 1. Ana sınıfa hp ve power alanları eklendi (Rastgele belirleniyor)
        self.hp = random.randint(100, 150)
        self.power = random.randint(10, 25)

    async def fetch_data(self):
        """PokeAPI üzerinden Pokémon verilerini çeker."""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    self.name = data['forms'][0]['name'].capitalize()
                    self.img_url = data['sprites']['front_default']
                else:
                    self.name = "Pikachu"
                    self.img_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"

    # 2. info metodu güncellendi: Adı, CAN (hp) ve GÜÇ (power) bilgilerini gösterir
    def info(self):
        return f"📌 **{self.name}**\n👤 Eğitmen: @{self.pokemon_trainer}\n❤️ Can (HP): {self.hp}\n⚔️ Güç: {self.power}"

    # 3. Ana sınıftaki temel attack metodu
    async def attack(self, enemy):
        # Düşmanın Sihirbaz (Wizard) olup olmadığını ve kalkan kullanıp kullanmadığını kontrol etme
        if isinstance(enemy, Wizard):
            sans = random.randint(1, 5)
            if sans == 1:
                return f"🛡️ **@{enemy.pokemon_trainer}** kişisinin Sihirbaz Pokémon'u bir kalkan kullandı ve saldırıyı engelledi!"

        # Normal Saldırı Mantığı
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"⚔️ Pokémon eğitmeni @{self.pokemon_trainer}, @{enemy.pokemon_trainer}'ne saldırdı!\n📉 @{enemy.pokemon_trainer}'nin kalan sağlığı: {enemy.hp}"
        else:
            enemy.hp = 0
            return f"🏆 Pokémon eğitmeni @{self.pokemon_trainer}, @{enemy.pokemon_trainer}'ni yendi!"


# 4 & 5. Fighter (Dövüşçü) Alt Sınıfı
class Fighter(Pokemon):
    async def attack(self, enemy):
        super_guc = random.randint(5, 15)  # Süper vuruş bonusu
        self.power += super_guc
        sonuc = await super().attack(enemy)
        self.power -= super_guc  # Gücü normal haline geri getiriyoruz
        return sonuc + f"\n🥊 **Dövüşçü Pokémon süper saldırı kullandı! Eklenen güç:** +{super_guc}"


# 4 & 5. Wizard (Sihirbaz) Alt Sınıfı
class Wizard(Pokemon):
    async def attack(self, enemy):
        # Sihirbaz saldırısını super() ile ana sınıftan alır
        return await super().attack(enemy)
