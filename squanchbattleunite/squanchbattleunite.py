from redbot.core import commands
from redbot.core import Config
import json
from pathlib import Path
import os
import random
import discord
import ast
import copy

from redbot.core.bot import Red
from redbot.core.utils import menus

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

RARITY_STONE_DICT = {
    1 : "m",
    2 : "mh",
    3 : "mhi",
    4 : "mhio"
}

RARITY_STONE_EMOJI_DICT ={
    1 : "<:goutm:739730447612903444>",
    2 : "<:goutmh:739735718745735169>",
    3 : "<:goutmhi:739735891903512587>",
    4 : "<:goutmhio:739736420503257090>"
}

RARITY_COLOR_DICT = {
    1 : 0x694a39,
    2 : 0xadadc0,
    3 : 0xdabf7e,
    4 : 0xa6dfff
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
            "characters" : [],
            "stones" : {
                "m" : 0,
                "mh" : 0,
                "mhi" : 0,
                "mhio" : 0
            }
        }
        self.config.register_user(**default_user)

    @commands.command()
    async def pull(self, ctx, rates=None):
        """Pull"""
        await self.get_pull(ctx)

    @commands.command()
    async def chars(self, ctx):
        """Chars"""
        try: 
            async with self.config.user(ctx.author).characters() as characters:
                current_characters = characters
            
            CHAR_DICT = {
                "◀️" : menus.prev_page,
                "⏹️" : menus.close_menu,
                "▶️" : menus.next_page
            }

            pages = self.create_character_pages(ctx, current_characters)
            if len(pages) > 1:
                await menus.menu(ctx, pages=pages, controls=CHAR_DICT)
            else:
                await ctx.send(embed=pages[0])
        except IndexError:
            await self.error(ctx, "You have no characters to display. Please use the .pull command!")
    
    @commands.command()
    async def clear(self, ctx):
        async with self.config.user(ctx.author).characters() as characters:
            characters.clear()

    @commands.command()
    async def stones(self, ctx):
        stones = await self.config.user(ctx.author).stones()
        title = "{}'s Finnathese Stones".format(ctx.author.name)
        message = "{} {} | {} {} | {} {} | {} {}".format(RARITY_STONE_EMOJI_DICT[1], stones["m"], \
                                                         RARITY_STONE_EMOJI_DICT[2], stones["mh"], \
                                                         RARITY_STONE_EMOJI_DICT[3], stones["mhi"], \
                                                         RARITY_STONE_EMOJI_DICT[4], stones["mhio"]   
                                                         )
        await self.message(ctx, title, message, "You can spend these stones with .finna to trade up to higher guaranteed rarities.")

    @commands.command()
    async def finna(self, ctx, rarity: str):
        try:
            rarity = rarity.lower()
            stones = await self.config.user(ctx.author).stones()
            needed_stones = 0
            current_stones = 0

            if rarity == "m":
                needed_stones = 15
            elif rarity == "mh":
                needed_stones = 13
            elif rarity == "mhi":
                needed_stones = 10
            elif rarity == "mhio":
                needed_stones = 6

            current_stones = stones[rarity]
            if current_stones >= needed_stones:
                if rarity == "m":
                    rates = [3, 19, 100]
                elif rarity == "mh":
                    rates = [3, 100, -1]
                else:
                    rates = [100, -1, -1]
                await self.get_pull(ctx, rates)
            else:
                await self.error (ctx, "You need {} more {} Finnathese Stones to complete this Finna Pull.".format(needed_stones-current_stones, rarity.upper()))
        except KeyError:
            await self.error(ctx, "You have provided an invalid rarity of Finnathese Stones.")

    async def get_pull(self, ctx, rates=None):
        summon_rarity = self.summon_rate(random.randint(1,100)) if rates is None else self.summon_rate(random.randint(1,100), rates) 
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
        message= ""
        if await self.check_for_dupes(ctx, summon_character[0]) == True:
            stones = await self.config.user(ctx.author).stones()
            stones[RARITY_STONE_DICT[summon_character[1]["rarity"]]] += 1
            await self.config.user(ctx.author).stones.set(stones)
            message="{} You have already pulled this character. You have received 1{}!".format(ctx.author.mention, RARITY_STONE_EMOJI_DICT[summon_character[1]["rarity"]])
        else:
            async with self.config.user(ctx.author).characters() as characters:
                characters.append(summon_character[0])
            
        file = discord.File(os.path.join(os.path.dirname(__file__), summon_character[1]["imagepath"]), summon_character[1]["imagename"])
        embed = discord.Embed(title="{}".format(summon_character[1]["name"]), description="**Rarity: {} | Element: {}**".format(RARITY_DICT[summon_character[1]["rarity"]], ELEMENT_DICT[summon_character[1]["element"]]),color=RARITY_COLOR_DICT[summon_character[1]["rarity"]])
        embed.set_image(url="attachment://{}".format(summon_character[1]["imagename"]))
        embed.set_footer(text="Pulled by {}".format(ctx.author.name), icon_url=ctx.author.avatar_url)
        
        await ctx.send(file=file, embed=embed,content=message)

    async def message(self, ctx, title, message, footer=""):
        embed = discord.Embed(title=title, description=message, color=ctx.me.colour)
        embed.set_footer(text=footer)

        await ctx.send(embed=embed)

    async def error(self, ctx, message):
        file = discord.File(os.path.join(os.path.dirname(__file__), "images/PakEDerm.png"), "PakEDerm.png")
        embed = discord.Embed(title="Error", description=message, color=discord.Color.red())
        embed.set_thumbnail(url="attachment://PakEDerm.png")
        embed.set_footer()

        await ctx.send(embed=embed, file=file)

    def summon_rate(self, num, rates=[3,19,30]):
        #3% Default
        if num <= rates[0]:
            return 4
        #7% Default
        elif num <= rates[1]:
            return 3
        #20% Default
        elif num <= rates[2]:
            return 2
        #70% Default
        else:
            return 1


    def get_character_pool(self, num):
        character_pool = []
        for key in self.characters:
            if self.characters[key]["rarity"] == num:
                character_pool.append([key, self.characters[key]])
        return character_pool

    def get_character_info(self, num):
        return self.characters[num]

    def create_character_pages(self, ctx, characters):
        embed = discord.Embed(title="{}'s Characters".format(ctx.author.name),color=ctx.author.color)
        char_num = 1
        page_num = 0
        pages = []
        for character in characters:
            char_info = self.get_character_info(character)
            embed.add_field(name="{}. {}".format(char_num+(page_num*15), char_info["name"]), value="{} {}".format(ELEMENT_DICT[char_info["element"]], RARITY_DICT[char_info["rarity"]]))
            char_num += 1
            if char_num >= 16:
                pages.append(copy.deepcopy(embed))
                embed.clear_fields()
                page_num += 1
                char_num = 1
        if char_num != 1:
            empty_spaces = (char_num-1) % 3
            if empty_spaces == 2:
                empty_spaces = 1
            elif empty_spaces == 1:
                empty_spaces = 2
            for x in range(empty_spaces):
                embed.add_field(name="⠀", value="⠀")
            pages.append(copy.deepcopy(embed))
        page_num = 1
        for page in pages:
            page.set_footer(text="Page {} of {}".format(page_num, len(pages)))
            page_num += 1
        return pages

    async def check_for_dupes(self, ctx, character):
        async with self.config.user(ctx.author).characters() as characters:
            if character in characters:
                return True
            else:
                return False
            
    


        