import aiohttp
import asyncio
from pokemon import Pokemon  # pokemon.py dosyanızdan içe aktarın

class Pokemon:
    def __init__(self, pokemon_number):
        self.pokemon_number = pokemon_number
        self.name = None
        self.hp = 0
        self.attack = 0
        self.types = []
        self.weight = 0
        self.base_experience = 0
        self.img_url = None


async def fetch_data(self):
        """API'den tüm verileri tek seferde çeker ve niteliklere atar."""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # Temel Nitelikler
                    self.name = data['forms'][0]['name'].capitalize()
                    self.weight = data['weight'] / 10  # kg cinsine çevrim
                    self.base_experience = data['base_experience']
                    self.img_url = data['sprites']['front_default']
                    
                    # Türleri Alma (List Comprehension)
                    self.types = [t['type']['name'] for t in data['types']]
                    
                    # İstatistikleri (Stats) Alma
                    for stat in data['stats']:
                        if stat['stat']['name'] == 'hp':
                            self.hp = stat['base_stat']
                        elif stat['stat']['name'] == 'attack':
                            self.attack = stat['base_stat']
                else:
                    self.name = "Pikachu"
                    self.hp = 35
                    self.attack = 55
                    self.types = ["electric"]

def get_info(self):
        """Pokémon'un detaylı özetini döndürür."""
        types_str = ", ".join(self.types)
        return (f"📌 **{self.name}**\n"
                f"❤️ Can (HP): {self.hp}\n"
                f"⚔️ Saldırı: {self.attack}\n"
                f"🏷️ Tür(ler): {types_str}\n"
                f"⚖️ Ağırlık: {self.weight} kg\n"
                f"⭐ Başlangıç XP: {self.base_experience}")

    def get_img(self):
        """Görsel URL'sini döndürür."""
        return self.img_url

def train(self, exp_gain):
        """Pokémon'u eğiterek saldırı gücünü ve deneyimini artırır."""
        self.attack += int(exp_gain * 0.2)
        self.base_experience += exp_gain
        print(f"{self.name} eğitildi! Yeni Saldırı Gücü: {self.attack}")

    def take_damage(self, damage):
        """Pokémon'un hasar almasını sağlar."""
        self.hp = max(0, self.hp - damage)
        print(f"{self.name} {damage} hasar aldı. Kalan Can: {self.hp}")



class Pokemon:
    def __init__(self, pokemon_number):
        self.pokemon_number = pokemon_number
        self.name = None
        self.hp = 0
        self.attack = 0
        self.types = []
        self.weight = 0
        self.base_experience = 0
        self.img_url = None

    async def fetch_data(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    self.name = data['forms'][0]['name'].capitalize()
                    self.weight = data['weight'] / 10
                    self.base_experience = data['base_experience']
                    self.img_url = data['sprites']['front_default']
                    self.types = [t['type']['name'] for t in data['types']]
                    
                    for stat in data['stats']:
                        if stat['stat']['name'] == 'hp':
                            self.hp = stat['base_stat']
                        elif stat['stat']['name'] == 'attack':
                            self.attack = stat['base_stat']

    def get_info(self):
        types_str = ", ".join(self.types)
        return (f"📌 **{self.name}**\n"
                f"❤️ Can (HP): {self.hp}\n"
                f"⚔️ Saldırı: {self.attack}\n"
                f"🏷️ Tür(ler): {types_str}\n"
                f"⚖️ Ağırlık: {self.weight} kg")

    def train(self, exp_gain):
        self.attack += int(exp_gain * 0.2)
        self.base_experience += exp_gain

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

async def main():
    my_pokemon = Pokemon(25)
    
    # 2. API verilerini yükle
    await my_pokemon.fetch_data()
    
    # 3. Bilgileri ve görseli yazdır
    print(my_pokemon.get_info())
    print("Görsel URL:", my_pokemon.img_url)
    
    # 4. Nitelik değiştirme metotlarını dene
    print("\n--- Eğitim Süreci ---")
    my_pokemon.train(50)
    print(f"Yeni Saldırı Gücü: {my_pokemon.attack}")

if __name__ == "__main__":
    asyncio.run(main())
