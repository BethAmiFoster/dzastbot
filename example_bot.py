import discord
import random
id_me = 257906842942832640
id_sad = 340493057390804993

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None
#džastbot v1.79 src

class MyClient(discord.Client):

  async def on_ready(self):
    print('gay {0.user}'.format(client))
    
    


  #async def on_message_delete(mess):

    #global snipe_message_content
    #global snipe_message_author
    #global snipe_message_id

    #snipe_message_content = mess.content
    #snipe_message_author = mess.author.id
    #snipe_message_id = mess.id
    #await asyncio.sleep(60)

    #if mess.id == snipe_message_id:
        #snipe_message_author = None
       # snipe_message_content = None
       # snipe_message_id = None
    
    
  #async def snipe(message):
    #if snipe_message_content==None and message.content.lower().find('snipe') != -1:
        #await message.channel.send("Theres nothing to snipe.")
    #else:
      #  embed = discord.Embed(description=f"{snipe_message_content}")
      #  embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
     #   embed.set_author(name= f"<@{snipe_message_author}>")
       # await message.channel.send(embed=embed)
        #return


  async def on_message(self, msg):
     if msg.author == client.user:
        return
        
     if msg.content.lower().find(':roach:') != -1 and msg.author.id != 694239905018281985 and msg.author.id != 695724819932643379 and msg.author.id !=696740734098866258 and msg.author.id !=695337101876789309:
         await msg.channel.send('<a:roach:660777026692579329>')
     #if msg.content.lower().find('testrnd') != -1 and msg.guild.id != 340493057390804993:
       #  variable = [
        #     'ancar.jpg',
         #    'quote.png',
          #   'creedoo.png',]
      #   await msg.channel.send(file=discord.File(random.choice(variable))
     if msg.content.lower().find('sad') != -1 and msg.guild.id != 340493057390804993:
         await msg.add_reaction('<:FBSaddery:375297208288804875>')
     if msg.content.lower().find(':garfidel:') != -1 and msg.author.id != 694239905018281985 and msg.author.id != 695724819932643379 and msg.author.id !=696740734098866258 and msg.author.id !=695337101876789309:
         await msg.channel.send('<a:garfielff:695367117385498685>')
     if msg.content.lower().find(':angery:') != -1 and msg.author.id != 694239905018281985 and msg.author.id != 695724819932643379 and msg.author.id !=696740734098866258 and msg.author.id !=695337101876789309:
         await msg.channel.send('<a:angery:695355908867489902>')
     if msg.content.lower().find(':rgbgarfidel:') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send('<a:rgbgarfidel:695367135006031993>')
     if msg.content.lower().find('banana') != -1 and msg.author.id != 694239905018281985 and msg.author.id != 695724819932643379 and msg.author.id !=696740734098866258:
         await msg.add_reaction('<:bananaDog:613393044460273684>')  
     if msg.content.lower().find('ssx') != -1 and msg.author.id == 257906842942832640:
         await msg.channel.send('dž') 
     if msg.content.lower().find('//update') != -1 and msg.author.id == 257906842942832640:
         await msg.channel.send('git add . /n git commit -am "lol" /n git push heroku master')
     if msg.content.lower().find('You just advanced to level') != -1:
         await msg.channel.send('yay111 he really do be leveling up doe 😳😳😳')
     if msg.content.lower().find('ancar') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('ancar.jpg'))
     if msg.content.lower().find('//sanchez') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('sanchez.mp3'))
     if msg.content.lower().find('//bs') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send('https://youtu.be/2uREIGawrvI') 
     #if msg.content.lower().find('dz!pizzabot') != -1:
         #await msg.channel.send('no')        
     if msg.content.lower().find('https://discord.gg/7bzadzA') != -1:
         await msg.channel.send('stfu stupid spambot') 
     if msg.content.lower().find('depressing') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('quote.png'))
     if msg.content.lower().find('phantom') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('quote.png'))
     if msg.content.lower().find('creedoo') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('creedoo.png'))
     if msg.content.lower().find('jojo') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('jojo.mp4'))
     if msg.content.lower().find('switch') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('switch.png'))
     if msg.content.lower().find('cat') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('cat.png'))
     if msg.content.lower().find('//data') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('data.png'))
     if msg.content.lower().find('//irr') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send(file=discord.File('20201221_153250.jpg'))
     if msg.content.lower().find('funny') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send('https://cdn.discordapp.com/attachments/702620924783886336/773354751370067968/video0.mp4') 
     if msg.content.lower().find('vtuber') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send('https://cdn.discordapp.com/attachments/644226511381069824/817003185955668038/Vtubers.mp4') 
     if msg.content.lower().find('wonder') != -1 and msg.author.id == 351773647871934466:
         await msg.channel.send('no you cant')
     if msg.content.lower().find('can we') != -1 and msg.author.id == 351773647871934466:
         await msg.channel.send('no we cant')
     if msg.content.lower().find('possible') != -1 and msg.author.id == 351773647871934466:
         await msg.channel.send('no you cant')
     if msg.content.lower().find('is there') != -1 and msg.author.id == 351773647871934466:
         await msg.channel.send('no there is not')
     if msg.content.lower().find('maybe') != -1 and msg.author.id == 351773647871934466:
         await msg.channel.send('no you cant')
     if msg.content.lower().find('last') != -1 and msg.author.id == 351773647871934466:
         await msg.channel.send('check yourself im not your mom')
     if msg.content.lower().find('get some help') != -1 and msg.author.id == 351773647871934466:
         await msg.channel.send('no u')
     if msg.content.lower().find('//help') != -1 and msg.author.id !=695337101876789309:
         await msg.channel.send('```Here is the command/feature list: \n Meme response stuff: \n //irr - Your post/This discussion meme \n "funny" - yes \n :roach: - Hoes Mad roach emoji \n :garfidel: - Garfield emoji \n //data - dont ask to ask \n :angery: - Angery emoji \n :rgbgarfidel: - RGB Garfield emoji \n //sanchez - inside joke only 10 people would get \n //bs - Bullshit \n //help - Shows this message \n Other features: \n Adds reactions to text which contains words sad or banana. \n Responds with a picture to words "Ancar" "Creedoo" "Phantom" "Switch" "Jojo" "Vtuber" and "Depressing"```')

     #if msg.author.id != 257906842942832640:
         #await msg.channel.send('sadra shut up')
client = MyClient(status = discord.Status.idle, activity = discord.Game('//help'))
client.run('you wish')
