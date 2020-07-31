from redbot.core import commands

class SquanchBattleUnite(commands.Cog):
    """Squanch Battle UNITE is a MHIO-based gacha game."""

    @commands.command()
    async def test(self, ctx):
        """test"""
        await ctx.send("test!");