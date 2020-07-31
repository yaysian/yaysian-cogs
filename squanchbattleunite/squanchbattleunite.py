from redbot.core import commands
import json
from pathlib import Path
import os
import random
import discord
import ast

from redbot.core.bot import Red

ELEMENT_DICT = {
    "beef": "https://cdn.discordapp.com/emojis/737481976512118816.png?v=1",
    "gout": "https://cdn.discordapp.com/emojis/737482102487908432.png?v=1",
    "squanch": "https://cdn.discordapp.com/emojis/737482123778457671.png?v=1",
    "fake": "https://cdn.discordapp.com/emojis/737482077473079366.png?v=1",
    "platano": "https://cdn.discordapp.com/emojis/737482113619591179.png?v=1",
    "bitch": "https://cdn.discordapp.com/emojis/737482048591233105.png?v=1"
}

RARITY_DICT = {
    1 : "https://cdn.discordapp.com/emojis/738662293117730830.png?v=1",
    2: "https://cdn.discordapp.com/emojis/738662323442679848.png?v=1",
    3: "https://cdn.discordapp.com/emojis/738662345219375205.png?v=1",
    4: "https://cdn.discordapp.com/emojis/738662375401586749.png?v=1"
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
            self.bot.characters = json.loads(data_file.read())

    @commands.command()
    async def test(self, ctx):
        """test"""
        await ctx.send("test!")

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
        file = discord.File(os.path.join(os.path.dirname(__file__), summon_character["imagepath"]), summon_character["imagename"])
        embed = discord.Embed()
        embed.set_image(url="attachment://{}".format(summon_character["imagename"]))
        embed.set_author(name="{}".format(summon_character["name"]), icon_url=ELEMENT_DICT[summon_character["element"]])
        embed.set_footer(text=RARITY_NAME_DICT[summon_character["rarity"]],icon_url=RARITY_DICT[summon_character["rarity"]])

        await ctx.send(file=file, embed=embed)

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
        for key in self.bot.characters:
            if self.bot.characters[key]["rarity"] == num:
                character_pool.append(self.bot.characters[key])
        return character_pool

        