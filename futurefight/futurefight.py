import discord
from discord.ext import commands
import datetime

class FutureFight:
    """Useful commands for Marvel: Future Fight."""
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def daily(self,ctx):
        """Returns how long until daily reset."""
        current_time = datetime.datetime.now()
        # Set hour of daily reset here. Default is in EST.
        reset_hour = 10
        daily_reset = datetime.datetime(year=current_time.year,month=current_time.month,day=current_time.day,hour=reset_hour,minute=00,second=0,microsecond=0)
        
        if current_time.hour > reset_hour:
            daily_reset = daily_reset + datetime.timedelta(days=1)
        time_remaining = daily_reset - current_time
        
        total_seconds = int(time_remaining.total_seconds())
        hours, remainder = divmod(total_seconds,60*60)
        minutes, seconds = divmod(remainder, 60)
        
        str = 'Time Until Daily Reset: **{} Hours, {} Minutes, {} Seconds**'.format(hours, minutes, seconds)
        em = discord.Embed(title='Daily Reset',description=str,colour=self.get_bot_color(ctx))
        
        await self.bot.send_message(ctx.message.channel, embed=em)
    
    @commands.command(pass_context=True)
    async def weekly(self,ctx):
        """Returns how long until weekly reset."""
        current_time = datetime.datetime.now()
        print(current_time)
        # Set hour of weekly reset here. Default is in EST.
        reset_hour = 20
        day_deficit = 0
        
        if current_time.weekday() < 3:
            day_deficit = 3 - current_time.weekday()
        elif current_time.weekday() > 3:
            day_deficit = 10 - current_time.weekday()
        
        weekly_reset = datetime.datetime(year=current_time.year,month=current_time.month,day=current_time.day,hour=reset_hour,minute=00,second=0,microsecond=0) + datetime.timedelta(days=day_deficit)
        time_remaining = weekly_reset - current_time
        
        total_seconds = int(time_remaining.total_seconds())
        days, remainder = divmod(total_seconds,60*60*24)
        hours, remainder = divmod(remainder,60*60)
        minutes, seconds = divmod(remainder, 60)
        
        str = 'Time Until Weekly Reset: **{} Days, {} Hours, {} Minutes, {} Seconds**'.format(days,hours, minutes, seconds)
        em = discord.Embed(title='Weekly Reset',description=str,colour=self.get_bot_color(ctx))
        
        await self.bot.send_message(ctx.message.channel, embed=em)
    
    def get_bot_color(self,ctx):
        member = ctx.message.server.get_member(self.bot.user.id)
        return member.color

def setup(bot):
    bot.add_cog(FutureFight(bot))