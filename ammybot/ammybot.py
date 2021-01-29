from redbot.core import commands
from redbot.core.bot import Red
from redbot.core import Config
import random
import discord
import os

clayton = ['On another note seriously has there ever been a game in the FGC blown up tech/combo wise more so than I did with DBFZ? All the most hype combos, craziest stuff in the game is just people retweeting my stuff, or trying to do a different variation of something I did. Goku double supers, sparking loops, gohans bomb loops, cells hop, looping trunks auto combos. Go on and on and on... all that stuff I posted first, hell a lot of it MONTHS ago on srk when people were saying this game is to basic has no combos... Seriously, I say that with no ego.. or well a healthy ego.. but all people are doing any time I see anything for this game right now, is stuff I did, or just assists stuff. Seriously that is insane. Bandai should have paid me for this.',
           'Main ideas that hopefully(...*crickets chirp*.. ya thats not happening)should be grasped from this. Assuming of course that we want to be able to be at a height where we can double super. So this can potentially put us in a conundrum if obviously we have to assume not all combos start from the ground (whether other people posting videos only want to do combos that start from teh ground or not.. rolls eyes  )for say something like the double down ki blast links. Which easily let you get a good height for the double super...So generally speaking better to go for one. Also of course although ki to kamehameha does more than down hard to hurricane kick, realistically in longer combos its not possible.',
           'On another note,  what a time to be alive that people would be seemingly making youtube accounts just to promote other youtubers on my page saying that no one needs to watch my videos just to watch these other guys. You know im having flash backs to years ago when a certain game was big and there was a back lash against my videos in comments people trying to say they were fake combos and i was cheating to do them. Japanese sites would post my stuff, but american sites would refuse to. Trying to get my stuff down etc, and then of course certain youtubers ended up becoming more famous. Funny. And the fact its happening a second time now is making it pretty curious to me. Dont under estimate what people will do for youtube money I guess if its them actually doing it. Ill pray its just random "fans" and not the actual people. But hey  I said it before even when I was winning those tournaments back as a kid, get that good that you can make money at video games and youll see there is politics even in video games.',
           'On a final note whats up with people coming into my videos trying to promote their videos, and then just showing off different variations of what I did and saying my videos are worse? Like dude, acting like I did a jump in, and you started with a medium, or switching one button around does not make your combo different or better. Or make you creative. Its crazy to think I have had to block so many people just because of combo videos on my page. Try to come up with your own stuff, try to actual build a foundation. Honestly speaking I am not creatively threatened right now if you can even use that word by anything anyone is putting out right now. So no one needs to try to promote their stuff as something new, and whats more try to promote your stuff in my comments and say my shit sucks when you are doing less than me and have never come up with anything but have a boner because you started a combo with less of a damage buffer but do other wise the exact same combo after watching my video... really?',
           'Anyway theres lots of shady FGC stories I could tell but point is, I like games more than I like the community. And I dont even like games that much anymore. So thats why I try to associate with people in it very rarely.  You know theres lots of people that all they talk about is how much they hate this game or they hate this and that, and then yet I still hear about them going to every tournament just to lose, just to complain. Well when I said I was gonna quit. I did. Didnt want to be one of those people that ended up hating something but kept coming back. So I decided I can randomly play video games by myself online, or randomly at a friends and I dont have to be by the people that make it unfun. And im fine with that.',
           ]
ike = [
    'https://cdn.discordapp.com/attachments/271499861696839680/565696206215577630/20190226_144209.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565696359521583110/IMG_-opi21n.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565696521710993408/20190410_163856.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565696587138072597/20190313_205003.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565696640657260546/20190306_170740.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565696674887106570/20190304_163403.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565696762707443712/20190122_085749.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565697027686793217/20190326_112959.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565697224483536906/20190305_161146.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565698026858086430/received_406899413389393.jpeg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565698125864370196/20190226_152526.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565698170214940673/received_388315081976788.jpeg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565698236765962280/20190111_130452.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565698351870246932/received_229959021054692.jpeg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565698446368178176/20181122_184146.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565699082866393109/IMG_8939.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565699180413321237/45276212_3415971889339_6735429131619532800_o.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565699268757815296/20180924_115118.jpg',
    'https://cdn.discordapp.com/attachments/271499861696839680/565699765682044938/received_1054892028022108.jpeg',
    'https://cdn.discordapp.com/attachments/271499861696839680/743133328659578961/ikecar.png',
]


class AmmyBot(commands.Cog):
    """AmmyBot Commands"""

    def __init__(self, bot: Red):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices separated by 'or'. Ex.) !choose this or that or maybe this"""
        string = list(choices)
        choiceList = []
        choice = ''
        if string and len(string) > 1:
            for word in string:
                if word == 'or':
                    if choice:
                        choiceList.append(choice)
                    choice = ''
                else:
                    choice += word + ' '
            if choice:
                choiceList.append(choice)
            if len(choiceList) > 1:
                await ctx.send(random.choice(choiceList))
            else:
                await ctx.send('```\nUsage: !choose something or something else or another thing ...\n```')
        else:
            await ctx.send('```\nUsage: !choose something or something else or another thing ...\n```')

    @commands.command(name='rns')
    async def rns(self, ctx):
        """"""
        await ctx.send(':rotating_light::rotating_light::rotating_light: WEE WOO WEE WOO WEE WOO :rotating_light::rotating_light::rotating_light: YOU ARE BEING DETAINED :cop::skin-tone-1::cop::skin-tone-1::cop::skin-tone-1: FOR BEING AWAKE DURING REAL NIGGA HOURS :clock1::ok_hand::skin-tone-1::smirk: PLEASE SHOW ME YOUR REAL NIGGA REGISTRATION :pray::skin-tone-1::pencil: BY SMASHING THE MOTHAFUCCIN LIKE BUTTON :speak_no_evil::raised_hands::skin-tone-2::fire::fire: REAL NIGGAS ONLY!! IT DONT MATTER IF YOU UP TRAPPING OR WHAT :sweat_drops::sweat_drops::weary::weary::100::100::100:')

    @commands.command(name='bully')
    async def bully(self, ctx):
        """"""
        await ctx.send('https://cdn.discordapp.com/attachments/85176687381196800/179404570143883265/6-4aQ-Qp_400x400.png')

    @commands.command(name='tech')
    async def tech(self, ctx):
        """"""
        await ctx.send('http://tinyimg.io/i/bgxg1vI.png')

    @commands.command(name='ty4c')
    async def ty4c(self, ctx):
        """"""
        await ctx.send('Thank you for contributing and not going off discussion.')

    @commands.command(name='destroyed')
    async def destroyed(self, ctx):
        """"""
        await ctx.send('http://i.imgur.com/BW4wOGK.png')

    @commands.command(name='pupper')
    async def pupper(self, ctx):
        """"""
        await ctx.send('http://i.imgur.com/hK96rUd.jpg')

    @commands.command(name='doggo')
    async def doggo(self, ctx):
        """"""
        await ctx.send('http://i.imgur.com/7cEXbxd.jpg')

    @commands.command(name='smooch')
    async def smooch(self, ctx):
        """"""
        await ctx.send('http://i.imgur.com/U59d9.gif')

    @commands.command(name='tilt')
    async def tilt(self, ctx):
        """"""
        await ctx.send('http://i.imgur.com/sv8KQZA.png')

    @commands.command(name='gaijin')
    async def gaijin(self, ctx):
        """"""
        await ctx.send('http://i.imgur.com/6BvDG2b.gif')

    @commands.command(name='toptier')
    async def toptier(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/0poiSAQ.jpg")

    @commands.command(name='doomgene')
    async def doomgene(self, ctx):
        """"""
        result = "Got a bunch of people that got animosity against DOOM cuz their S BUTTON is bigger than em. These are the guys thats jealous because they don't carry, they don't possess ACTUAL DEFENSE, they don't possess that SETPLAY. Keep being jealous. Keep wondering your wife is asking for proper defense, keep wondering why your girlfriend asks for mashed back throws and wishing to be stomped on by this Latverian ruler with huge metal feet that'll smother them until the point where they can feel each and every last spectacle of their wakeup options getting raw foot dived or hit confirmed into the maziodyne loop that spews out! Keep saying fraud, keep saying scrub. COME ON. You strangefags. You love it. You love this shit, I'LL BE THAT PLAYER. I'LL BE THAT PLAYER, yep with that hard kick pressure. Enjoy it, have your woman take this full TAC infinite, she's imagining huge metal shock gloves, why do you think your bitches play support characters? Because you don't possess that PROPER NEUTRAL. That's why you're upset, no Neutral= Anger. You're upset with this setplay, these rhino Full Schedule sequences. That's why you use press buttons every wakeup. I get it!"
        await ctx.send(result)

    @commands.command(name='rayx2', aliases=['ray', 'rayray'])
    async def rayx2(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/0egQnmI.jpg")

    @commands.command(name='book')
    async def book(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/LKf6epG.png")

    @commands.command(name='joespecial')
    async def joespecial(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/kgSlJ2E.png")

    @commands.command(name='school')
    async def school(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/feUA1mN.png")

    @commands.command(name='stfu')
    async def stfu(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/q8BrtiN.jpg")

    @commands.command(name='nice')
    async def nice(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/CYvLTVJ.jpg")

    @commands.command(name='beaned')
    async def beaned(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/NkD56cv.jpg")

    @commands.command(name='free')
    async def free(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/g7dFBcs.jpg")

    @commands.command(name='blockin')
    async def blockin(self, ctx):
        """"""
        await ctx.send("https://pbs.twimg.com/media/CuwROasVYAAtuig.jpg")

    @commands.command(name='boat')
    async def boat(self, ctx):
        """"""
        await ctx.send("https://cdn.discordapp.com/attachments/85176687381196800/234006823781269506/sfv.gif")

    @commands.command(name='shitpost')
    async def honor(self, ctx):
        """"""
        await ctx.send("Apparently. When I play a fighting game. Like the Free Tekken game for PS3, I feel like… I am filled with honor. I knock a guy down to the ground, and I back away so they can get back up. Like the honorable martial arts fighter would. But… I guess no one in the fucking world understands this concept since everyone from 7 ranks above me or first starting the game all do the same cheap tactics like spam the invincible attack or spam you with attacks that never give you a chance to do anything.\n\nWith that I say… Where is the honor in a martial arts fighting game, Like tekken (sorta) or Virtual Fighter. When in a martial arts fight, You bow to your opponet as a sign of honor. since you cant do that in a game, the best you can do is crouch when the match starts, only leading to about 50+ hits to the face. Fuck everyone who plays fighting games like its a competition. Fighting games should be played with a sense of respect.\n\nI have no respect for anyone I fight with, but I will still play the game by my code of honor.")

    @commands.command(name='pad')
    async def pad(self, ctx):
        """"""
        await ctx.send("https://cdn.discordapp.com/attachments/85176687381196800/257666440180662274/post_post.jpg")

    @commands.command(name='fray')
    async def fray(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/moKRH9U.gif")

    @commands.command(name='dab')
    async def dab(self, ctx):
        """"""
        await ctx.send("https://cdn.discordapp.com/attachments/85176687381196800/268051894373580801/Betty.png")

    @commands.command(name='wack')
    async def wack(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/dOOyIFb.png")

    @commands.command(name='midwack')
    async def midwack(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/Sh3Tjds.jpg")

    @commands.command(name='block')
    async def block(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/1Zs854D.png")

    @commands.command(name='work')
    async def work(self, ctx):
        """"""
        await ctx.send("http://i.imgur.com/taHvVio.png")

    @commands.command(name='banlat')
    async def banlat(self, ctx):
        """"""
        await ctx.send("http://i.giphy.com/6FeRQGbt8Fb2.gif")

    @commands.command(name='xrd')
    async def xrd(self, ctx):
        """"""
        await ctx.send("https://cdn.discordapp.com/attachments/85176687381196800/281499092629323777/lazy_11.jpg")

    @commands.command(hidden=True)
    async def nut(self, ctx):
        if ctx.message.channel.id == '271499861696839680':
            await ctx.send("https://i.imgur.com/8cRz5Bh.png")

    @commands.command(name='clayton')
    async def clayton(self, ctx):
        """"""
        await ctx.send(random.choice(clayton))

    @commands.command()
    async def gs(self, ctx):
        """That is some good shit."""
        await ctx.send(':ok_hand: :eyes: :ok_hand: :eyes: :ok_hand: :eyes: :ok_hand: :eyes: :ok_hand: :eyes: good shit go౦ԁ sHit :ok_hand: thats :heavy_check_mark: some good :ok_hand: :ok_hand: shit right :ok_hand: :ok_hand: there :ok_hand: :ok_hand: :ok_hand: right :heavy_check_mark: there :heavy_check_mark: :heavy_check_mark: if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ :100: :ok_hand: :ok_hand: :ok_hand: НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ :ok_hand: :ok_hand: :ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand: :ok_hand: Good shit')

    @commands.command(aliases=["ike!"])
    async def ike(self, ctx):
        """"""
        await ctx.send(random.choice(ike))

    @commands.command()
    async def matt(self, ctx):
        """"""
        await ctx.send("https://cdn.discordapp.com/attachments/271499861696839680/798418117998805003/Ela7VDfXYAIaKKA.jpg")
