import discord
from discord.ext import commands
import datetime
import random
import urllib

char_list = ['America Chavez',\
             'Heimdall',\
             'Skurge',\
             'Titania',\
             'Absorbing Man',\
             'Mysterio',\
             'Rhino',\
             'Kraven',\
             'Lizard',\
             'Sandman',\
             'Whiplash',\
             'Mantis',\
             'Hellcat',\
             'Ghost Rider (Robbie Reyes)',\
             'Maximus',\
             'Crystal',\
             'Gorgon',\
             'Karnak',\
             'Moon Girl',\
             'Medusa',\
             'Hawkeye (Kat Bishop)',\
             'Hela',\
             'Hogun',\
             'Volstagg',\
             'Fandral',\
             'Ulik',\
             'Hellstorm',\
             'Ancient One',\
             'Kaecilius',\
             'Wong',\
             'Baron Mordo',\
             'Misty Night',\
             'Shang-Chi',\
             'Squirrel Girl',\
             'Songbird',\
             'Hulkling',\
             'Wiccan',\
             'White Tiger',\
             'Captain America (Sharon Rogers)',\
             'Sin',\
             'Moon Knight',\
             'Crossbones',\
             'Thor (Jane Foster)',\
             'Ms. Marvel (Kamala Khan)',\
             'Hulk (Amadeus Cho)',\
             'Silk',\
             'Spider-Gwen',\
             'Spider-Man (Miles Morales)',\
             'Jessica Jones',\
             'Elsa Bloodstone',\
             'Warwolf',\
             'Phil Coulson',\
             'Lash',\
             'Lincoln Campbell',\
             'Deathlok',\
             'Sif',\
             'Daisy Johnson',\
             'She-Hulk',\
             'Singularity',\
             'Sister Grimm',\
             'Yellowjacket',\
             'Wasp',\
             'Giant-Man',\
             'Ant-Man',\
             'Ronan',\
             'Nebula',\
             'Yondu',\
             'Hulkbuster (Iron Man Mark 44)',\
             'Bullseye',\
             'Kingpin',\
             'Venom',\
             'Elektra',\
             'Angela',\
             'Black Bolt',\
             'Black Panther',\
             'Star-Lord',\
             'Iron Fist',\
             'Luke Cage',\
             'Agent 13',\
             'Punisher',\
             'Winter Soldier',\
             'Falcon',\
             'Vision',\
             'War Machine',\
             'Captain Marvel',\
             'Red Hulk',\
             'Mockingbird',\
             'Hawkeye',\
             'Drax',\
             'Destroyer',\
             'Malekith',\
             'M.O.D.O.K.',\
             'Green Goblin',\
             'Doctor Octopus',\
             'Daredevil',\
             'Red Skull',\
             'Loki',\
             'Ultron',\
             'Gamora',\
             'Groot',\
             'Spider-Man',\
             'Black Cat',\
             'Thor',\
             'Black Widow',\
             'Blade',\
             'Rocket Raccoon',\
             'Ghost Rider',\
             'Iron Man',\
             'Hulk',\
             'Captain America']
             
ult_list = ['Anti-Man',\
             'Nova',\
             'Blue Marvel',\
             'America Chavez',\
             'Quasar']
             
ult_six_list = ['Anti-Man',\
             'Nova',\
             'Blue Marvel']
             
class FutureFight:
    """Useful commands for Marvel: Future Fight."""
    
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(pass_context=True)
    async def daily(self,ctx):
        """Returns how long until daily reset."""
        current_time = datetime.datetime.utcnow()
        reset_hour = 15
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
        current_time = datetime.datetime.utcnow()
        reset_hour = 1
        day_deficit = 0
        
        if current_time.weekday() < 4:
            day_deficit = 4 - current_time.weekday()
        elif current_time.weekday() > 3:
            day_deficit = 11 - current_time.weekday()
        
        weekly_reset = datetime.datetime(year=current_time.year,month=current_time.month,day=current_time.day,hour=reset_hour,minute=00,second=0,microsecond=0) + datetime.timedelta(days=day_deficit)
        time_remaining = weekly_reset - current_time
        
        total_seconds = int(time_remaining.total_seconds())
        days, remainder = divmod(total_seconds,60*60*24)
        hours, remainder = divmod(remainder,60*60)
        minutes, seconds = divmod(remainder, 60)
        
        str = 'Time Until Weekly Reset: **{} Days, {} Hours, {} Minutes, {} Seconds**'.format(days,hours, minutes, seconds)
        em = discord.Embed(title='Weekly Reset',description=str,colour=self.get_bot_color(ctx))
        
        await self.bot.send_message(ctx.message.channel, embed=em)
        
    @commands.command(pass_context=True)
    async def pull10(self,ctx):
        """Simulation of the BEST DEAL EVER! 30% Chance to get a guaranteed 6 Star of The Ultimates or Nova."""
        found_rs = False
        found_ms = False
        rs = ''
        ms = ''
        for emoji in ctx.message.server.emojis:
            if emoji.name == 'rs':
                found_rs = True
                rs = str(emoji)
            elif emoji.name == 'ms':
                found_ms = True
                ms = str(emoji)
                
        if found_rs == False or found_ms == False:
            await self.bot.say(':hourglass_flowing_sand: Please wait a couple of seconds before reattempting this command while the custom emojis are installed.')  
            await self.upload_emojis(ctx, found_rs, found_ms)
            
        else:
            pull_list = char_list + ult_list
            guaranteed_ult = True if random.randint(1,10) < 3 else False
            five_star = False
            desc_str = 'Guaranteed 6{}**THE ULTIMATES** or **NOVA**!'.format(rs) if guaranteed_ult == True else 'One 5{} character guaranteed!'.format(rs)
            em = discord.Embed(title='Ultimate Hero Chest',description=desc_str,colour=self.get_bot_color(ctx))
            em.set_thumbnail(url='http://i.cubeupload.com/4emBko.png')
            
            for x in range(0,9):
                char_name = random.choice(pull_list)
                ultimates = False
                rank = self.get_pull_rate(random.randint(1,100))
                
                if guaranteed_ult == False and rank >= 5:
                    five_star = True
                if char_name in ult_list:
                    ultimates = True
                rank_str = self.get_star_string(rank, ultimates, rs, ms)
                em.add_field(name=char_name,value=rank_str,inline=True)
                
            if guaranteed_ult == True:
                em.add_field(name=random.choice(ult_six_list),value=self.get_star_string(6, True, rs, ms),inline=True)
            elif five_star == False:
                em.add_field(name=random.choice(pull_list),value=self.get_star_string(5, False, rs, ms),inline=True)
            else:
                em.add_field(name=random.choice(pull_list),value=self.get_star_string(random.randint(3,6),False, rs, ms),inline=True)
                
            await self.bot.send_message(ctx.message.channel,embed=em)
    
    async def upload_emojis(self, ctx, rs, ms):
        url1 = 'http://vignette.wikia.nocookie.net/future-fight/images/e/ec/RankStar.png'
        url2 = 'http://vignette.wikia.nocookie.net/future-fight/images/d/da/MasteryStar.png'
        try:
            if rs == False:
                with urllib.request.urlopen(url1) as url:
                    with open('temp.jpg','wb') as f:
                        f.write(url.read())
                    f = open('temp.jpg','rb')
                    await self.bot.create_custom_emoji(server=ctx.message.server,name='rs',image=f.read())
            if ms == False:
                with urllib.request.urlopen(url2) as url:
                    with open('temp.jpg','wb') as f:
                        f.write(url.read())
                    f = open('temp.jpg','rb')
                    await self.bot.create_custom_emoji(server=ctx.message.server,name='ms',image=f.read())
            await self.bot.say(':white_check_mark: Custom Emojis have been successfully installed.')  
        except Exception:
            await self.bot.say('`There was an error uploading the custom emojis. This command requires Manage Emoji permissions.`')
            
    def get_pull_rate(self, num):
        #3%
        if num <= 3:
            return 6
        #6%
        elif num <= 9:
            return 5
        #39%
        elif num <= 48:
            return 4
        #52%
        else:
            return 3
            
    def get_star_string(self, num, ultimates, rs, ms):
        str = ''
        star = ms if ultimates == True else rs
        for y in range(num):
                str += star
        return str
        
    def get_bot_color(self,ctx):
        member = ctx.message.server.get_member(self.bot.user.id)
        return member.color
    
def setup(bot):
    bot.add_cog(FutureFight(bot))