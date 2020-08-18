from redbot.core import commands
from redbot.core.bot import Red
from redbot.core import Config
import discord
import os

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

class GCP(commands.Cog):
    
    def __init__ (self, bot: Red):
        super().__init__()
        self.bot = bot
        self.credentials = GoogleCredentials.get_application_default()
        self.service = discovery.build('compute', 'v1', credentials=self.credentials)
        self.config = Config.get_conf(self, identifier=1234567890)
        default_guild = {
            'project': '',
            'zone' : '',
            'instance': ''
        }
        self.config.register_guild(**default_guild)

    @commands.group()
    async def gcp(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.error(ctx, "Invalid GCP command passed...")

    @gcp.command()
    async def set(self, ctx, property : str, value: str):
        try:
            if property == "zone":
                await self.config.guild(ctx.guild).zone.set(value)
            elif property == "project":
                await self.config.guild(ctx.guild).project.set(value)
            elif property == "instance":
                await self.config.guild(ctx.guild).instance.set(value)
            else:
                raise ValueError("Incorrect propery name.")
            await self.message(ctx, "Success", "Properly set the property.")
        except Exception as e:
            print(e)
            await self.error(ctx, "Could not properly set the property.")

    @gcp.command()
    async def start(self, ctx):
        project = await self.config.guilt(ctx.guild).project()
        zone = await self.config.guilt(ctx.guild).zone()
        instance = await self.config.guilt(ctx.guild).instance()
        try:
            request = self.service.instances().start(project=project, zone=zone, instance=instance)
            response = request.execute()
            file = discord.File(os.path.join(os.path.dirname(__file__), "crumb.jpg"), "crumb.jpg")
            if response:
                await self.message(ctx, "Success", "Here is your crumb of cloud.", "", file, "crumb.jpg")
            else:
                await self.error(ctx, "Received no response from Google Cloud Platform API.")
        except:
            await self.error(ctx, "Could not properly start up GCP Compute Instance.")

    async def message(self, ctx, title, message, footer="", file=None, file_name=""):
        embed = discord.Embed(title=title, description=message, color=ctx.me.colour)
        embed.set_footer(text=footer)

        if file is None:
            embed.set_thumbnail(url="attachment://{}".format(file_name))
            await ctx.send(embed=embed, file=file)
        else:
            await ctx.send(embed=embed)

    async def error(self, ctx, message):
        embed = discord.Embed(title="Error", description=message, color=discord.Color.red())
        embed.set_footer()

        await ctx.send(embed=embed)

