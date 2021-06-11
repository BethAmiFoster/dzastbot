import discord
import os
from discord.ext import commands
import random
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



class MyClient(discord.Client):



    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        channel = client.get_channel(695014904381440092)
        randomlist = (['im back baby', 'https://cdn.discordapp.com/attachments/606550060284510218/837688700564406323/im_back_baby.mp4',])
        response = random.choice(randomlist)
        await channel.send(response)
    async def on_message_edit(message_before, message_after, message):
        if message.channel.id == 660314906972651530 and not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
          await message.delete()
            
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.author.bot: return
        if message.content.startswith('//dzhelp') and message.channel.id !=660314906972651530:
           embedhelp=discord.Embed(title="Džastbot v2.128 help menu", description="Welcome to džastbot help menu, here is a small command/feature list:")
           embedhelp.set_author(name="Džastbot", url="https://cdn.discordapp.com/attachments/695014904381440092/836329019292516392/sus16.png", icon_url="https://cdn.discordapp.com/avatars/695337101876789309/199d18d7311452261f0e3dcfe49fad32.png")
           embedhelp.add_field(name="//megadrop", value="//megadrop - posts link with every nfs build i (JA) could find up to 2020 xmas ", inline=False)
           embedhelp.add_field(name="//irr", value="//irr - Your post/This discussion meme", inline=False)
           embedhelp.add_field(name="//beytah", value="//beytah - for annoying fucks who cant read pins", inline=False)
           embedhelp.add_field(name="//data", value="//data - dont ask to ask", inline=False)
           embedhelp.add_field(name="//sanchez", value="//sanchez - inside joke only 10 people would get", inline=False)
           embedhelp.add_field(name="//bs", value="//bs - Bullshit", inline=False)
           embedhelp.add_field(name="//dzhelp", value="//dzhelp - Shows this message", inline=False)
           embedhelp.add_field(name="//changelog", value="//changelog - changelog", inline=False)
           embedhelp.add_field(name="//funny", value="funny - yes", inline=False)
           embedhelp.add_field(name="Other features:", value="Responds with a picture/video to words `Ancar` `Creedoo` `Phantom` `Switchuwu` `Jojo` `Vtuber` `Sus` `Among us` `Amogus` `Amongus` `Pimps at sea` `Catgirl` `Toast` and `Depressing`", inline=False)
           embedhelp.add_field(name="Misc:", value="//update and //loopback - things exclusive for JA", inline=False)
           embedhelp.set_footer(text="fuck discord fr")
           await message.reply(embed=embedhelp, mention_author=True)
        if message.content.startswith('//changelog') and message.channel.id !=660314906972651530:
           embed=discord.Embed(title="Džastbot changelog")
           embed.set_author(name="Džastbot", icon_url="https://cdn.discordapp.com/avatars/695337101876789309/199d18d7311452261f0e3dcfe49fad32.png", url="https://cdn.discordapp.com/attachments/695014904381440092/836329019292516392/sus16.png")
           embed.add_field(name="reserved for future update", value="2.128 - embed rework, zoomer repellent upd and no more crayon chewing", inline=False)
           embed.add_field(name="2.125-2.127 - zoomer repellent", value="2.124 - sus", inline=False)
           embed.add_field(name="2.123 - toast", value="2.122 - //funny upd", inline=False)
           embed.add_field(name="2.121 - trigger updates thanks to upside down fuck and grzegorz brzęczyszczykiewicz and everyone else", value="2.120 - internal token upd", inline=False)
           embed.add_field(name="2.119 - no more cat", value="2.118 - jojo and pimps at sea update", inline=False)
           embed.add_field(name="2.116 - im back baby", value="2.115 - smiley channel edits update", inline=False)
           embed.add_field(name="2.114 - moar sus pic", value="2.113 - pimp at sea update", inline=False)
           embed.add_field(name="2.111 - embeds update and bots blacklisted", value="2.109 - smiley channel", inline=False)
           embed.add_field(name="2.102 - added //megadrop", value="2.99-2.100 - more sus pics", inline=False)
           embed.add_field(name="2.98 - more triggers for sus pics", value="2.97 - pimps at sea update", inline=False)
           embed.add_field(name="2.96 - more sus pics", value="2.94 - added //beytah", inline=False)
           embed.add_field(name="2.92 - enabled smiley channel code", value="2.85 - 2.91 - working on smiley channel revival, although disabled (code works though) plus one bugfix for sus response",inline=False)
           embed.add_field(name="2.85 - changed //help to //dzhelp", value="2.84 - updated //help and //changelog textbox", inline=False)
           embed.add_field(name="2.83 - added //changelog command", value="2.82 - added more sus pics", inline=False)
           embed.add_field(name="2.81 - updated //help textbox", value="CANT I JUST LEAVE THIS EMPTY", inline=False)
           embed.set_footer(text="fuck discord fr")
           await message.reply(embed=embed, mention_author=True)
        if message.content.lower() == ('sus') != -1 and message.channel.id !=660314906972651530:
            randomlist = (['sus1.jpg', 'sus2.png', 'sus3.mp4', 'sus4.png', 'sus5.jpg', 'sus6.png', 'sus7.png', 'sus8.jpg', 'sus9.png', 'sus10.jpg','sus11.mp4', 'sus12.png', 'sus13.mp4', 'sus14.mp4', 'sus15.mp4', 'sus16.png', 'sus17.jpg', 'sus18.mov', 'sus19.png',])
            response = random.choice(randomlist)
            await message.channel.send(file=discord.File(response))
        if message.content.lower() == ('amogus') != -1 and message.channel.id !=660314906972651530:
            randomlist = (['sus1.jpg', 'sus2.png', 'sus3.mp4', 'sus4.png', 'sus5.jpg', 'sus6.png', 'sus7.png', 'sus8.jpg', 'sus9.png', 'sus10.jpg','sus11.mp4', 'sus12.png', 'sus13.mp4', 'sus14.mp4', 'sus15.mp4', 'sus16.png', 'sus17.jpg', 'sus18.mov', 'sus19.png',])
            response = random.choice(randomlist)
            await message.channel.send(file=discord.File(response))
        if message.content.lower() == ('amongus') != -1 and message.channel.id !=660314906972651530:
            randomlist = (['sus1.jpg', 'sus2.png', 'sus3.mp4', 'sus4.png', 'sus5.jpg', 'sus6.png', 'sus7.png', 'sus8.jpg', 'sus9.png', 'sus10.jpg','sus11.mp4', 'sus12.png', 'sus13.mp4', 'sus14.mp4', 'sus15.mp4', 'sus16.png', 'sus17.jpg', 'sus18.mov', 'sus19.png',])
            response = random.choice(randomlist)
            await message.channel.send(file=discord.File(response))
        if message.content.lower() == ('among us') != -1 and message.channel.id !=660314906972651530:
            randomlist = (['sus1.jpg', 'sus2.png', 'sus3.mp4', 'sus4.png', 'sus5.jpg', 'sus6.png', 'sus7.png', 'sus8.jpg', 'sus9.png', 'sus10.jpg','sus11.mp4', 'sus12.png', 'sus13.mp4', 'sus14.mp4', 'sus15.mp4', 'sus16.png', 'sus17.jpg', 'sus18.mov', 'sus19.png',])
            response = random.choice(randomlist)
            await message.channel.send(file=discord.File(response))
        if message.content.startswith('//data') and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('data.png'))
        if message.content.startswith('//irr') and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('20201221_153250.jpg'))
        if message.content.lower().find('//update') != -1 and message.author.id == 257906842942832640 and message.channel.id !=660314906972651530:
            await message.channel.send('```heroku login\n git add . \n git commit -am "lol" \n git push heroku master```')
        if message.content.lower().find('ancar') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('ancar.jpg'))
        if message.content.startswith('//sanchez') and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('sanchez.mp3'))
        if message.content.startswith('//megadrop') and message.channel.id !=660314906972651530:
            await message.channel.send('Mega folder with every nfs build I could find til 2020 xmas: <https://mega.nz/folder/u18FCRpQ#mQoqpPz_vAi5JgJeGhxoZA>')
        if message.content.lower().find('//bs') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send('https://youtu.be/2uREIGawrvI')
        if message.content.lower().find('depressing') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('quote.png'))
        if message.content.lower().find('phantom') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('quote.png'))
        if message.content.lower().find('creedoo') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('creedoo.png'))
        if message.content.lower().find('jojo') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            randomlist = (['jojo.mp4', 'jojo2.mp4',])
            response = random.choice(randomlist)
            await message.channel.send(file=discord.File(response))
        if message.content.lower().find('switchuwu') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('switch.png'))
        if message.content.lower().find('catgirl') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('cat2.png'))
        if message.content.lower().find('toast') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send(file=discord.File('toast.png'))
        if message.content.lower() == ('//funny') and message.channel.id !=660314906972651530:
            await message.channel.send('https://cdn.discordapp.com/attachments/702620924783886336/773354751370067968/video0.mp4')
        if message.content.lower() == ('vtuber') != -1 and message.author.id !=695337101876789309 and message.channel.id !=660314906972651530:
            await message.channel.send('https://cdn.discordapp.com/attachments/644226511381069824/817003185955668038/Vtubers.mp4')
       # if message.content.lower().find('wonder') != -1 and message.author.id == 351773647871934466 and message.channel.id !=660314906972651530:
            #await message.channel.send('no you cant')
        #if message.content.lower().find('can we') != -1 and message.author.id == 351773647871934466 and message.channel.id !=660314906972651530:
            #await message.channel.send('no we cant')
        #if message.content.lower().find('possible') != -1 and message.author.id == 351773647871934466 and message.channel.id !=660314906972651530:
            #await message.channel.send('no you cant')
       # if message.content.lower().find('is there') != -1 and message.author.id == 351773647871934466 and message.channel.id !=660314906972651530:
           # await message.channel.send('no there is not')
        #if message.content.lower().find('maybe') != -1 and message.author.id == 351773647871934466 and message.channel.id !=660314906972651530:
            #await message.channel.send('no you cant')
        #if message.content.lower().find('last') != -1 and message.author.id == 351773647871934466 and message.channel.id !=660314906972651530:
            #await message.channel.send('check yourself im not your mom')
        #if message.content.lower().find('get some help') != -1 and message.author.id == 351773647871934466 and message.channel.id !=660314906972651530:
            #await message.channel.send('no u')
        if message.content.lower().find('pimps at sea') != -1 and message.channel.id !=660314906972651530:
            pimpslist =['https://media.discordapp.net/attachments/644226511381069824/828733114464993300/pingdariogreggio.gif', 'https://cdn.discordapp.com/attachments/487367223808098304/836337916023406662/PimpsAtSeaDarioGreggio.mp4', 'https://cdn.discordapp.com/attachments/839090722464071720/842457988085317632/pimps_ds.png', 'https://cdn.discordapp.com/attachments/487367223808098304/842238106819231744/PimpsAtSeaMadMen.mp4', 'https://media.discordapp.net/attachments/839090722464071720/842190590841585694/pas-amog-us.png', 'https://media.discordapp.net/attachments/839090722464071720/842085327219982336/lego-pimps.png', 'https://cdn.discordapp.com/attachments/839090722464071720/840010604445564958/passponge.mp4',]
            response = random.choice(pimpslist)
            await message.channel.send(response)
        if message.channel.id == 660314906972651530 and not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
            await message.delete() # idk if its done this way but who cares
        if message.content.startswith('//beytah') and message.channel.id !=660314906972651530:
            await message.channel.send('https://cdn.discordapp.com/attachments/705829278851268649/795080310576119848/ezgif-7-fe5f3082509e.gif')
        if message.content.startswith('//loopback') and message.author.id == 257906842942832640 and message.channel.id !=660314906972651530:
            await message.channel.send('```pactl load-module module-loopback latency_msec=1```') 
        if message.content.lower().find('uwu') != -1 or message.content.lower().find('owo') != -1 or message.content.lower().find('x3') != -1:
            await message.add_reaction('🛑')


 
client = MyClient(status = discord.Status.idle, activity = discord.Game('v2.128; //dzhelp'))
client.run(TOKEN)
