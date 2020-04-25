import discord
import re
from discord.ext import commands
from discord.ext.commands import Bot
import random

bot = discord.Client()

beegangslang = ['Adapt. Improvise. Bee Gang.',
                'Bee Gang world domination is going to happen! Kill them with love.',
                'To help, and to bee helped.', 
                '#beegang > #peargang. Eric told me so!',
                'I love #beegang!',
                'Our beemotes are top tier!',
                '*buzz* *buzz*',
                'We have a Large Swarm of Mom Bees.',
                'If I had dreams, I would dream of #beegang',
                ':bee: :bee:',
                '...and Eric is salad, confirmed! :white_check_mark:']

german = ['I am *Beeling Bot* = Ich bin *Beeling Bot*',
         'Bee = Biene',
         'Beekeeper = Imkerin / Imker',
         'Hive = Bienenstock',
         'Honey = Honig',
         'Beeswax = Bienenwax',
         ':bee: Gang World Domination Planning Server = Bienengang Weltherrschaftsplanungsserver']

germanswear = ['Damn = Mist',
              'Fuck = Fuck',
              'Shit = Scheiße',
              'Shit = Kacke',
              'Asshole = Arschloch']

french = ["Honey = miel",
          "Beekeeper = apriculteur (trice)",
          "Hive = ruche",
          "Beeswax = cire d'abeille",
          ":bee: Gang World Domination Planning Server = abeille gang preparation du domination de la monde serveur",
          "Bee = abeille"]

aussieslang = ["Arvo = Afternoon (S'Arvo – this afternoon)",
               "Avo = Avocado",
               "Barbie = Barbecue",
               "Bludger = Someone who's lazy, generally also who relies on others (when it's someone who relies on the state they're often called a 'dole bludger'; also Bludging - slacking off/being lazy)",
               "Brekky = Breakfast",
               "Buggered = Exhausted",
               "Choccy Biccy/Bikky = Chocolate Biscuit",
               "Coldie = Beer. 'Come over for a few coldie's mate.'",
               "Crack the shits = Getting angry at someone or something",
               "Crikey = an expression of surprise",
               "Crook = Being ill (I'm crook); a criminal (he's a crook)",
               "Fair Dinkum = 'Fair Dinkum?' ... 'Fair Dinkum!' = Honestly? ... Yeah honestly!",
               "Flat out = Really busy = 'Flat out like a lizard drinking' = As busy as a bee",
               "Hard yakka = Hard work",
               "Maccas = McDonalds",
               "Rellie / Rello = Relatives",
               "Ripper = 'You little ripper' = That’s fantastic mate!",
               "Sanger = Sandwich",
               "Servo = Service Station / Garage",
               "Sickie = a sick day off work, or 'to pull a sickie' would be to take a day off when you aren't actually sick",
               "Stoked = Happy, Pleased",
               "Straya = Australia",
               "Strewth = An exclamation of surprise",
               "Thongs = Flip Flops. Do not be alarmed if your new found Australian friend asks you to wear thongs to the beach. They are most likely expressing their concern of the hot sand on your delicate feet.",
               "True Blue = Genuinely Australian",
               "U-ie = to take a U-Turn when driving",
               "Woop Woop = middle of nowhere 'he lives out woop woop'"]

@bot.event
async def on_ready():
    print('Login was successful.')

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    ##mommabee = discord.utils.get(discord.User, name = 'Clouded.Cat', discriminator = '2700')
   
    newclist = []
    commandlist = {'!hello': 'Hello '+str(message.author.mention)+'! I love you <:honeyheart:696740294934265976>',
                   '!abby': 'We love Abby. <:honeyheart:696740294934265976>',
                   '!beebot': 'I love my Bee Bot beeling!',
                   '!bedtime': "Every bee needs it's beeauty sleep. :zzz:",
                   '!sleep': 'You need to go to beed. :zzz:',
                   '!german': random.choice(german),
                   '!gswear': random.choice(germanswear),
                   '!french': random.choice(french),
                   '!beeligion': 'Praise the Celestial Bee Silvea, the Sentinel of Air.',
                   '!selfcare': 'Go to bed, stay hydrated, dont forget to eat, and do what u love.',
                   '!water':'Everyone, stay hydrated!',
                   '!panic':'*Where is Eric???*',
                   '!mom': '*Do not make me call our large swarm of mom bees!*',
                   '!callmom': 'Moooooom <@!548503002512752640>!!',
                   '!cute': 'Bee Gang cute.',
                   '!advice': 'Stay in drugs, eat your school and do not do vegetables.',
                   '!ilymods': 'We have god mods.',
                   '!homework': 'Everyone, do your homework!',
                   '!hydrate': 'hydrate or diedrate',
                   '!aussie': random.choice(aussieslang)}

    #newrlist = ['go to bed @someone']
    newrlist = []
    reactionlist = {'#beegang': random.choice(beegangslang)}
    
    for i in commandlist:
        newclist.append(i)
        if message.content.find(i) != -1:
            await message.channel.send(commandlist.get(i))

    for i in reactionlist:
        newrlist.append(i)
        if message.content.find(i) != -1:
            await message.channel.send(reactionlist.get(i))
    
    if message.content.startswith('!command'):
        embed = discord.Embed(title="Beeling Bot's Command List", description="Have fun trying some of these commands. And tell everyone to go to bed!", color=0xfed963)
        #embed.add_field(name="Beeling Bot knows some commands", value=newclist, inline=False)
        embed.add_field(name="Spred love and care about others", value="!abby, !beebot, !bedtime, !cute, !hydrate, !ilymods, !selfcare, !sleep, !water", inline=True)
        embed.add_field(name="Wanna know some fun facts?", value="!aussie, !french, !german, !gswear", inline=True)
        embed.add_field(name="Beeling Bot reacts to", value="#beegang", inline=False)
        embed.add_field(name="Miscellaneous commands", value="!advice, !beeligion, !callmom, !hello, !homework, !mom, !panic", inline=True)
        embed.add_field(name="Please bee careful with the !callmom command", value="...as it actually pings LSB.",inline=True)
        embed.set_image(url='https://cdn.discordapp.com/attachments/693338784124764193/693722855648526376/image0.png')
        await message.channel.send(embed=embed)
    
    # I need to fix the following thing??    
    #if message.content.find('Go'+'to'+'bed'):
    #    await message.channel.send('You really should try to sleep a bit. We will still bee here when you wake up. Also, our large swarm of mom bees will bee very proud. Goodnight! :star:')

with open('tokenbb', 'r') as file:
    token = file.read()

bot.run(token)
