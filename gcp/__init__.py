from .gcp import GCP

def setup(bot):
    bot.add_cog(GCP(bot))