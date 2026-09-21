import aiohttp
import random

class Pokemon:
    pokemons = {}  # Oluşturulan tüm Pokémon'ları saklayan sözlük

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 151)
        self.name = None
        self.img_url = None
        self.hp = random.randint(100, 150)
        self.max_hp = self.hp  # Can yenileme (heal) için maksimum canı saklıyoruz
        self.power = random.randint(10, 25)
        
        # Oyuncuyu sözlüğe kaydediyoruz
        Pokemon.pokemons[pokemon_trainer] = self

    async def fetch_data(self):
        """API üzerinden Pokémon verilerini çeker."""
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    self.name = data['forms'][0]['name'].capitalize()
                    self.img_url = data['sprites']['front_default']
                else:
                    self.name = "Pikachu"

    async def show_img(self):
        if not self.name:
            await self.fetch_data()
        return self.img_url

    async def info(self):
        if not self.name:
            await self.fetch_data()
        return f"📌 **{self.name}**\n👤 Eğitmen: @{self.pokemon_trainer}\n❤️ Can (HP): {self.hp}/{self.max_hp}\n⚔️ Güç: {self.power}"

    async def attack(self, enemy):
        # Düşman Wizard ise kalkan kullanma şansını kontrol et
        if isinstance(enemy, Wizard):
            sans = random.randint(1, 5)
            if sans == 1:
                return f"🛡️ **@{enemy.pokemon_trainer}** eğitmeninin Sihirbaz Pokémon'u kalkan kullandı ve saldırıyı engelledi!"

        # Normal Saldırı
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"⚔️ **@{self.pokemon_trainer}**, **@{enemy.pokemon_trainer}** kullanıcısına saldırdı!\n📉 @{enemy.pokemon_trainer} kalan canı: {enemy.hp}"
        else:
            enemy.hp = 0
            return f"🏆 **@{self.pokemon_trainer}**, **@{enemy.pokemon_trainer}** eğitmenini yendi!"

    def heal(self):
        """Ek Görev: Savaş sonrası Pokémon'un canını tamamen yeniler."""
        self.hp = self.max_hp
        return f"❤️ **@{self.pokemon_trainer}** eğitmeninin Pokémon'u tamamen iyileştirildi! Can: {self.hp}/{self.max_hp}"


class Fighter(Pokemon):
    async def attack(self, enemy):
        super_guc = random.randint(5, 15)
        self.power += super_guc
        sonuc = await super().attack(enemy)
        self.power -= super_guc  # Gücü eski haline getiriyoruz
        return sonuc + f"\n🥊 **Dövüşçü Pokémon süper saldırı kullandı!** Eklenen Güç: +{super_guc}"


class Wizard(Pokemon):
    async def attack(self, enemy):
        return await super().attack(enemy)


# Mantık kodunu kendi içinde test etme alanı
if __name__ == '__main__':
    import asyncio

    async def test():
        wizard = Wizard("kullanici1")
        fighter = Fighter("kullanici2")

        print(await wizard.info())
        print()
        print(await fighter.info())
        print()
        print(await fighter.attack(wizard))

    asyncio.run(test())
