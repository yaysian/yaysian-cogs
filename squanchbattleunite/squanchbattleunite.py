from redbot.core import commands
import json

from redbot.core.bot import Red

class SquanchBattleUnite(commands.Cog):
    """Squanch Battle UNITE is a MHIO-based gacha game."""

    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot
        self.characters = json.load(open("characters.json"))

    @commands.command()
    async def test(self, ctx):
        """test"""
        await ctx.send("test!")

    @commands.command()
    async def pull(self, ctx):
        """Pull"""
        await ctx.send(self.characters)


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
        