from .ammybot import AmmyBot


def setup(bot):
    bot.add_cog(AmmyBot(bot))
