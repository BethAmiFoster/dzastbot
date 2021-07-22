  
import discord
import os
#import praw
from discord.ext import commands
import random
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#bot = commands.Bot(description="test", command_prefix="!")

#reddit = praw.Reddit(client_id='4AI7G9lF3koPcQ',
                    # client_secret='Gbdk2cB2srbJm6a6CpIaW7NpQ3d3RQ',
                    # user_agent='post mirroring 0.1 by /u/JustAnyoneYT')

#@bot.command()
#async def meme():
 #   memes_submissions = reddit.subreddit('memes').hot()
 #   post_to_pick = random.randint(1, 10)
 #   for i in range(0, post_to_pick):
   #     submission = next(x for x in memes_submissions if not x.stickied)

 #   await bot.say(submission.url)


class MyClient(discord.Client):



    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        channel = client.get_channel(695014904381440092)
        randomlist = (['Codename Baka Shinji , Indev 1.0.5 Startup Complete. Online!', 'Guten Morgen!', 'https://cdn.discordapp.com/attachments/695014904381440092/867679459498262578/videoplayback.mp4', ])
        response = random.choice(randomlist)
        await channel.send(response)
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.author.bot: return
        if message.content.startswith('~help'):
           embedhelp=discord.Embed(title="Asuka's help menu", description="Welcome to my help menu!")
           embedhelp.set_author(name="Asuka")
           embedhelp.add_field(name="~help", value="Shows this help menu.", inline=False)
           embedhelp.add_field(name="~changelog", value="Shows my changelog.", inline=False)
           await message.reply(embed=embedhelp, mention_author=True)
        if message.content.startswith('~changelog'):
           embed=discord.Embed(title="My changelog")
           embed.set_author(name="Asuka")
           embed.add_field(name="1.0.6", value="Changed '~asukahelp' to '~help', fixed example_bot.py.", inline=False)
           embed.add_field(name="1.0.5", value="Updated example_bot.py", inline=False)
           embed.add_field(name="1.0.4", value="Changed Codename from 'Luna' to 'Baka Shinji'.", inline=False)
           embed.add_field(name="1.0.3", value="Fixed random startup code", inline=False)
           embed.add_field(name="1.0.2", value="Changed prefix from '//' to '~'.", inline=False)
           embed.add_field(name="1.0.1", value="Added command 'england', dislays image.", inline=False)
           embed.add_field(name="1.0.0", value="Asuka was born.", inline=False)
           await message.reply(embed=embed, mention_author=True)
        if message.content.startswith('england') and message.channel.id !=660314906972651530:
            await message.channel.send('https://media.discordapp.net/attachments/635144592534011958/867615725484244992/52a7r21gboc71.png')
client = MyClient(status = discord.Status.idle, activity = discord.Game('~help'))
client.run(TOKEN)
