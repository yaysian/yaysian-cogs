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
            'loss': 0,
            'winquote': "Do you hear it? ＴＨＥ　ＣＲＩＥＳ　ＯＦ　ＴＨＥ　ＥＡＲＴＨ"
        }
        self.config.register_user(**default_user)
        self.games = []

    @commands.command()
    async def battle(self, ctx):
        if ctx.message.mentions:
            if ctx.message.mentions[0].id != ctx.message.author.id:
                title = "Battle Request"
                message = f'{ctx.message.author.nick} has challenged {ctx.message.mentions[0].nick} to a **SQUANCH BATTLE!**\n\n⭕ to accept\n❌ to reject'
                footer = "Squanch Battle Resquanched"

                message = await self.message(ctx, title, message, footer)

                logic = {
                    'players': [ctx.message.author, ctx.message.mentions[0]],
                    'rolls': [0, 0],
                    'hp': [100, 100],
                    'message': message,
                    'started': False
                }

                self.games.append(logic)

                await self.set_reactions(message, REQUEST_EMOJIS)

    async def on_raw_reaction_add(self, payload):
        if self.games.size > 0:
            gameNum = self.isIngame(payload.user_id)
            if gameNum:
                if self.games[gameNum].message.id == payload.message_id:
                    if not self.games[gameNum].started:
                        # ACCEPT OR REJECT
                        print(payload.emoji)

    async def message(self, ctx, title, message, footer=""):
        embed = discord.Embed(
            title=title, description=message, color=ctx.me.colour)
        embed.set_footer(text=footer)

        return await ctx.send(embed=embed)

    async def set_reactions(self, message, emojis):
        for emoji in emojis:
            await message.add_reaction(emoji)

    def isIngame(self, id):
        result = False
        count = 0
        for game in self.games:
            for player in game.players:
                if player.id == id:
                    result = count
                count += 1
        return result
