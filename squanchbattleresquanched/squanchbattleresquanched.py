from redbot.core import commands
from redbot.core import Config
import discord

from redbot.core.bot import Red
from redbot.core.utils import menus

REQUEST_EMOJIS = ["⭕", "❌"]


class SquanchBattleResquanched(commands.Cog):
    """Squanch Battle Resquanched is a remaster of the original Squanch Battle."""

    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_user = {
            'win': 0,
            'loss': 0
        }
        default_guild = {
            'games': []
        }
        self.config.register_user(**default_user)
        self.config.register_guild(**default_guild)

    @commands.command()
    async def battle(self, ctx):
        if ctx.message.mentions:
            if ctx.message.mentions[0].id != ctx.message.author.id:
                logic = {
                    'players': [self.create_player(ctx.message.author), self.create_player(ctx.message.mentions[0])],
                    'rolls': [0, 0],
                    'hp': [100, 100]
                }

                async with self.config.guild(ctx.guild).games() as games:
                    games.append(logic)

                title = "Battle Request"
                message = f'{ctx.message.author.nick} has challenged {ctx.message.mentions[0].nick} to a **SQUANCH BATTLE!**\n\n⭕ to accept\n❌ to reject'
                footer = "Squanch Battle Resquanched"

                message = await self.message(ctx, title, message, footer)
                await self.set_reactions(message, REQUEST_EMOJIS)

    async def message(self, ctx, title, message, footer=""):
        embed = discord.Embed(
            title=title, description=message, color=ctx.me.colour)
        embed.set_footer(text=footer)

        await ctx.send(embed=embed)

    async def set_reactions(self, message, emojis):
        for emoji in emojis:
            await message.add_reaction(emoji)

    def create_player(self, player):
        return {
            'name': player.nick,
            'id': player.id,
        }
