import discord
import re
from discord.ext import commands
from discord.ext.commands import Bot
import random

bot = commands.Bot(command_prefix='$')

beegangslang = ['Adapt. Improvise. Bee Gang.',
                'Bee Gang world domination is going to happen! Kill them with love.',
                'To help, and to bee helped.', 
                '#beegang > #peargang. Eric told me so!',
                'I love #beegang!',
                'Our beemotes are top tier!',
                '*buzz* *buzz*',
                'Bees are friends, not food!',
                'We have a Large Swarm of Mom Bees.',
                'If I had dreams, I would dream of #beegang',
                ':bee: :bee:',
                '...and Eric is salad, confirmed! :white_check_mark:']

german = ['hello = Hallo',
         'I am *Beeling Bot* = Ich bin *Beeling Bot*',
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
    
    commandlist = {'!hello': 'Hello '+str(message.author.mention)+'! I love you :honeyheart:?',
                   '!test': 'I am still learning how to bot!',
                   '!beebot': 'I love my Bee Bot beeling!',
                   '#beegang': random.choice(beegangslang),
                   '!bedtime': 'Every bee needs its beeauty sleep. :zzz:',
                   '!sleep': 'You need to go to beed. :zzz:',
                   '!german': random.choice(german),
                   '!gswear': random.choice(germanswear),
                   '!beeligion': 'Praise the Celestial Bee Silvea, the Sentinel of Air.',
                   '!selfcare': 'Go to bed, stay hydrated, dont forget to eat, and do what u love',
                   '!water':'Everyone, stay hydrated!',
                   '!panic':'*Where is Eric???*'}
    
    for i in commandlist:
        if message.content.find(i) != -1:
            await message.channel.send(commandlist.get(i))
    
    if message.content.startswith('!command'):
        embed = discord.Embed(title="Beeling Bot", description="Have fun trying some of these commands. And tell everyone to go to bed!", color=0xfed963)
        embed.add_field(name="Beeling Bot knows some commands", value="!hello, !bedtime, !sleep, !german, !gswear, !mom, !beeligion, !water, !selfcare, !panic", inline=False)
        embed.add_field(name="Beeling Bot reacts to a few keywords", value="#beegang, go to bed @someone", inline=False)
        embed.set_image(url='https://cdn.discordapp.com/attachments/693338784124764193/693722855648526376/image0.png')
        await message.channel.send(embed=embed)
    
    if message.content.find('!mom') != -1:
        await message.channel.send('*Do not make me call your large swarm of mom bees*!')
                
        def check(m):
            return m.content == 'Mom!' and m.channel == message.channel

        msg = await bot.wait_for('message', timeout=10.0, check=check)
        await message.channel.send('@aLargeSwarmofBees, come here and help me!'.format(msg))
    
    # I need to fix the following thing??    
    #if message.content.find('Go'+'to'+'bed'):
    #    await message.channel.send('You really should try to sleep a bit '+message.mentions[0].mention+'. We will still be here when you wake up. Also, our large swarm of mom bees will be very proud. Goodnight! :star:')

with open('token', 'r') as file:
    token = file.read()

bot.run(token)
