
import discord
import os
from discord.ext import commands
import random
from dotenv import load_dotenv


client = commands.Bot(command_prefix = '~')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):

    #startup command

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        channel = client.get_channel(695014904381440092)
        randomlist = (['Codename Baka Shinji, Indev 1.1.0 Startup Complete. Online!', 'Guten Morgen!', 'https://cdn.discordapp.com/attachments/695014904381440092/867679459498262578/videoplayback.mp4', ])
        response = random.choice(randomlist)
        await channel.send(response)
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.author.bot: return

    #help command

        if message.content.startswith('~help'):
           embedhelp=discord.Embed(title="Asuka's help menu", description="Welcome to my help menu!")
           embedhelp.set_author(name="Asuka")
           embedhelp.add_field(name="~help", value="Shows this help menu.", inline=False)
           embedhelp.add_field(name="~changelog", value="Shows my changelog.", inline=False)
           embedhelp.add_field(name="~help", value="We gotta figure out how it works first.", inline=False)
           
           await message.reply(embed=embedhelp, mention_author=True)

    #changelog command

        if message.content.startswith('~changelog'):
           embed=discord.Embed(title="My changelog")
           embed.set_author(name="Asuka")
           embed.add_field(name="1.1.2", value="Added 'banana' and 'uwu, owo and x3 reactions'.", inline=False)
           embed.add_field(name="1.1.1", value="Added 'waifu' and 'jojo' commands, displays image.", inline=False)
           embed.add_field(name="1.1.0", value="Added '~hug' command.", inline=False)
           embed.add_field(name="1.0.6", value="Changed '~asukahelp' to '~help', fixed example_bot.py.", inline=False)
           embed.add_field(name="1.0.5", value="Updated example_bot.py", inline=False)
           embed.add_field(name="1.0.4", value="Changed Codename from 'Luna' to 'Baka Shinji'.", inline=False)
           embed.add_field(name="1.0.3", value="Fixed random startup code", inline=False)
           embed.add_field(name="1.0.2", value="Changed prefix from '//' to '~'.", inline=False)
           embed.add_field(name="1.0.1", value="Added command 'england', dislays image.", inline=False)
           embed.add_field(name="1.0.0", value="Asuka was born.", inline=False)
           await message.reply(embed=embed, mention_author=True)

    #hug command



    #image commands

        if message.content.startswith('england') and message.channel.id !=660314906972651530:
            await message.channel.send('https://media.discordapp.net/attachments/635144592534011958/867615725484244992/52a7r21gboc71.png')

        if message.content.startswith('waifu') and message.channel.id !=660314906972651530:
            await message.channel.send('https://cdn.discordapp.com/attachments/644226511381069824/867743649885454346/RDT_20210720_1018515839053802029751255.jpg')

        if message.content.startswith('jojo') and message.channel.id !=660314906972651530:
            await message.channel.send('https://cdn.discordapp.com/attachments/635144592534011958/867744369192599562/jojo.mp4')

    #reactions

        if message.content.lower().find('uwu') != -1 or message.content.lower().find('owo') != -1 or message.content.lower().find('x3') != -1:
            await message.add_reaction('😊')

        if message.content.lower().find('banana') != -1:
            await message.add_reaction('🍌')

    #bot online status and activity

client = MyClient(status = discord.Status.online, activity = discord.Game('Guten Morgen!'))
client.run(TOKEN)
