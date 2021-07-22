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
        channel = client.get_channel(635144592534011958)
        randomlist = (['Codename Luna, Indev 1.1 Startup Complete, Online!'])
        response = random.choice(randomlist)
        await channel.send(response)
    async def on_message_edit(message_before, message_after, message):
        if message.channel.id == 635144592534011958 and not all(map(lambda x: x == '😃', ''.join(message.content.split()))):
          await message.delete()
            
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.author.bot: return
        if message.content.startswith('//lunahelp') and message.channel.id !=660314906972651530:
           embedhelp=discord.Embed(title="Codename: Luna", description="Codename Luna, A bot by Wildcat and Tex")
           embedhelp.set_author(name="Codename: Luna", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://cdn.discordapp.com/attachments/635144592534011958/867438178021539840/20210722_020846.jpg")
           embedhelp.add_field(name="//megadrop", value="//megadrop - posts link with every nfs build i (JA) could find up to 2020 xmas ", inline=False)
           embedhelp.add_field(name="//irr", value="//irr - Your post/This discussion meme", inline=False)
           embedhelp.add_field(name="//beytah", value="//beytah - for annoying fucks who cant read pins", inline=False)
           embedhelp.add_field(name="//data", value="//data - dont ask to ask", inline=False)
           embedhelp.add_field(name="//sanchez", value="//sanchez - inside joke only 10 people would get", inline=False)
           embedhelp.add_field(name="//bs", value="//bs - Bullshit", inline=False)
           embedhelp.add_field(name="//lunahelp", value="//lunahelp - Shows this message", inline=False)
           embedhelp.add_field(name="//changelog", value="//changelog - changelog", inline=False)
           embedhelp.add_field(name="//funny", value="funny - yes", inline=False)
           embedhelp.add_field(name="Other features:", value="Responds with a picture/video to words `Ancar` `Creedoo` `Phantom` `Switchuwu` `Jojo` `Vtuber` `Sus` `Among us` `Amogus` `Amongus` `Pimps at sea` `Catgirl` `Toast` `A1ra/Aira/Sadra` `Tanner` and `Depressing`", inline=False)
           embedhelp.add_field(name="Misc:", value="//update and //loopback - things exclusive for JA", inline=False)
           embedhelp.set_footer(text="fuck discord fr")
           await message.reply(embed=embedhelp, mention_author=True)
        if message.content.startswith('//changelog') and message.channel.id !=660314906972651530:
           embed=discord.Embed(title="Codename: Luna changelog")
           embed.set_author(name="Codename: Luna", icon_url="https://cdn.discordapp.com/attachments/635144592534011958/867438178021539840/20210722_020846.jpg", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
           embed.add_field(name="1.1 Indev - Branding Change", inline=False)
           embed.add_field(name="1.0 Indev - Codename Luna Fork", inline=False)
           embed.add_field(name="2.131 - sadra and tanner update", value="2.128 - embed rework, zoomer repellent upd and no more crayon chewing", inline=False)
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
       
        if message.content.lower().find('uwu') != -1 or message.content.lower().find('owo') != -1 or message.content.lower().find('x3') != -1:
            await message.add_reaction('✔️')


 
client = MyClient(status = discord.Status.idle, activity = discord.Game('v1.1 Indev; //lunahelp'))
client.run(TOKEN)
