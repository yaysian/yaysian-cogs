from redbot.core import commands
from redbot.core import Config
import json
from pathlib import Path
import os
import random
import discord
import ast

from redbot.core.bot import Red

ELEMENT_DICT = {
    "beef": "<:beef:737481976512118816>",
    "gout": "<:gout:737482102487908432>",
    "squanch": "<:squanch:737482123778457671>",
    "fake": "<:fake:737482077473079366>",
    "platano": "<:platano:737482113619591179>",
    "bitch": "<:bitch:737482048591233105>"
}

RARITY_DICT = {
    1 : "<:mhoo:738662293117730830>",
    2: "<:mh:738662323442679848>",
    3: "<:mhi:738662345219375205>",
    4: "<:mhio:738662375401586749>"
}

RARITY_NAME_DICT = {
    1 : "Mhoo",
    2 : "Mini Hoo",
    3 : "Mega Hoo Incarnate",
    4 : "My Hoo Is Omega"
}

class SquanchBattleUnite(commands.Cog):
    """Squanch Battle UNITE is a MHIO-based gacha game."""

    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot
        json_path = os.path.join(os.path.dirname(__file__), "data/characters.json")
        with open(json_path, encoding='utf-8') as data_file:
            self.characters = json.loads(data_file.read())
        self.config = Config.get_conf(self, identifier=1234567890)
        default_user = {
            'user_data' : {
                'characters': []
            }
        }
        self.config.register_user(**default_user)

    @commands.command()
    async def pull(self, ctx):
        """Pull"""
        summon_rarity = self.summon_rate(random.randint(1,100))
        summon_pool = []
        summon_character = {}

        if summon_rarity == 1:
            summon_pool = self.get_character_pool(1)
        elif summon_rarity == 2:
            summon_pool = self.get_character_pool(2)
        elif summon_rarity == 3:
            summon_pool = self.get_character_pool(3)
        elif summon_rarity == 4:
            summon_pool = self.get_character_pool(4)

        summon_character = random.choice(summon_pool)
        file = discord.File(os.path.join(os.path.dirname(__file__), summon_character[1]["imagepath"]), summon_character[1]["imagename"])
        embed = discord.Embed(title="{}".format(summon_character[1]["name"]), description="**Rarity: {} | Element: {}**".format(RARITY_DICT[summon_character[1]["rarity"]], ELEMENT_DICT[summon_character[1]["element"]]))
        embed.set_image(url="attachment://{}".format(summon_character[1]["imagename"]))

        current_characters = self.config.user(ctx.author).user_data.characters()
        await self.config.user(ctx.author).user_data.characters.set(current_characters.append(summon_character[0]))
        await ctx.send(file=file, embed=embed)

    @commands.command()\
    async def chars(self, ctx):
        """Chars"""
        current_characters = self.config.user(ctx.author).user_data.characters()
        ctx.send(current_characters)

    def summon_rate(self, num):
        #3%
        if num <= 3:
            return 4
        #7%
        elif num <= 10:
            return 3
        #20%
        elif num <= 30:
            return 2
        #70%
        else:
            return 1

    def get_character_pool(self, num):
        character_pool = []
        for key in self.characters:
            if self.characters[key]["rarity"] == num:
                character_pool.append([key, self.characters[key]])
        return character_pool

        