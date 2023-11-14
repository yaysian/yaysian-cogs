from .ammybot import AmmyBot


async def setup(bot):
    await bot.add_cog(AmmyBot(bot))
