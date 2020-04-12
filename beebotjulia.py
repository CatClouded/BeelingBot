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
                   '!beebot': 'I love my Bee Bot beeling!',
                   '!bedtime': 'Every bee needs its beeauty sleep. :zzz:',
                   '!sleep': 'You need to go to beed. :zzz:',
                   '!german': random.choice(german),
                   '!gswear': random.choice(germanswear),
                   '!beeligion': 'Praise the Celestial Bee Silvea, the Sentinel of Air.',
                   '!selfcare': 'Go to bed, stay hydrated, dont forget to eat, and do what u love.',
                   '!water':'Everyone, stay hydrated!',
                   '!panic':'*Where is Eric???*',
                   '!mom': '*Do not make me call our large swarm of mom bees!*',
                   '!callmom': 'Moooooom <@!548503002512752640>!!',
                   '!cute': 'Bee Gang cute.'}

    newrlist = ['go to bed @someone']
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
        embed = discord.Embed(title="Beeling Bot", description="Have fun trying some of these commands. And tell everyone to go to bed!", color=0xfed963)
        embed.add_field(name="Beeling Bot knows some commands", value=newclist, inline=False)
        embed.add_field(name="Beeling Bot reacts to a few keywords", value=newrlist, inline=False)
        embed.set_image(url='https://cdn.discordapp.com/attachments/693338784124764193/693722855648526376/image0.png')
        await message.channel.send(embed=embed)
    
    # I need to fix the following thing??    
    if message.content.find('Go'+'to'+'bed') and message.mentions != []:
        await message.channel.send('You really should try to sleep a bit '+message.mentions[0].mention+'. We will still be here when you wake up. Also, our large swarm of mom bees will be very proud. Goodnight! :star:')

with open('tokenbb', 'r') as file:
    token = file.read()

bot.run(token)
