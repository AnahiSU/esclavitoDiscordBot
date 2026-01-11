import discord
from discord.ext import commands
import random 
import os
import webserver

intents = discord.Intents.default()
intents.message_content = True

DISCORD_TOKEN = os.environ['discordkey']

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():

    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('Pongsito')

@bot.command()
async def pendejo(ctx):
    await ctx.send('puto')

@bot.command()
async def talk(ctx, *, mess):
    await ctx.message.delete() 
    await ctx.send(mess)

@bot.command()
async def gatito(ctx):

    imgs = {
        1: "https://i.pinimg.com/736x/42/03/37/42033722deefe4f5e249107f56e26cbe.jpg",
        2: "https://i.pinimg.com/736x/10/bc/bd/10bcbdc51fdacda178fbf70267e19251.jpg",
        3: "https://i.pinimg.com/736x/bb/00/fb/bb00fbabd0a58d0bc918cb8bd5664837.jpg",
        4: "https://i.pinimg.com/736x/a2/e5/4d/a2e54d57a7d1080214a6ace3070058c9.jpg",
        5: "https://i.pinimg.com/736x/47/7e/ee/477eee2362bc01bc984b7987f7134b2e.jpg",
        6: "https://i.pinimg.com/736x/0c/7d/e5/0c7de5aa6e0cf848ffdd9553c768feea.jpg",
        7: "https://i.pinimg.com/736x/92/41/92/924192b2cdbec6802e7fe4229e2e1bd9.jpg",
        8: "https://i.pinimg.com/736x/f4/5e/fa/f45efa5796ddc72c6ef18a384bcde9d9.jpg",
        9: "https://i.pinimg.com/736x/4c/61/db/4c61db2801403466a0ffb10e2171297e.jpg",
        10: "https://i.pinimg.com/736x/96/e5/24/96e5243e32fd44789c6e52d55ab1234a.jpg",
        11: "https://i.pinimg.com/736x/a9/18/fc/a918fc8d3316cffc62a63c124fe4f15a.jpg"
    }

    num = random.randint(1, 11)
    url_gato = imgs[num]
    
    embed = discord.Embed(title="miau", color=0x0000FF)
    embed.set_image(url=url_gato)
    
    await ctx.send(content="Toma un gatito:", embed=embed)

@bot.command()
async def patito(ctx):

    imgs = {
        1: "https://i.pinimg.com/736x/84/ac/6d/84ac6d467c0a7c16cd28d2364bae7cc1.jpg",
        2: "https://i.pinimg.com/736x/b6/0e/91/b60e916285d363bb9f5ba9f68bd41391.jpg",
        3: "https://i.pinimg.com/736x/39/52/29/3952292f4cc051123848a7eff7317047.jpg",
        4: "https://i.pinimg.com/736x/b8/57/3a/b8573a09729b1fe189c109e16978bb1b.jpg",
        5: "https://i.pinimg.com/736x/a7/3d/c5/a73dc53d9ef4af7a02f1ec75e7bb5b98.jpg",
        6: "https://i.pinimg.com/736x/d0/aa/d2/d0aad27c5a1d62d86a1f13baf1b333af.jpg",
        7: "https://i.pinimg.com/736x/8d/91/1b/8d911b60413005b5b55eede38bb1fc77.jpg",
        8: "https://i.pinimg.com/736x/48/29/fc/4829fce4a571302942e1c0ccf35e7b77.jpg",
        9: "https://i.pinimg.com/736x/b4/e6/ad/b4e6ad2f346f9bdcf5682de37f4782a5.jpg",
        10: "https://i.pinimg.com/736x/42/96/13/429613d286507ae8969985357b8f4697.jpg",
        11: "https://i.pinimg.com/736x/4d/7a/5f/4d7a5f3aecdf83b2114135456cfeca76.jpg"
    }

    num = random.randint(1, 11)
    url_pato = imgs[num]
    
    embed = discord.Embed(title="quack", color=0xFFFF00)
    embed.set_image(url=url_pato)
    
    await ctx.send(content="Toma un patito:", embed=embed)

@bot.command()
async def saleLol(ctx):
    flag = random.randint(1,2)
    mss = "Si" if (flag == 1)  else "No, toca pasto"
    await ctx.send(content = mss)

@bot.command()
async def randomTeams(ctx, *, mss: str):
    members = [m.strip() for m in mss.split(',')]
    random.shuffle(members)

    len1 = len(members)//2

    await ctx.send("TEAM 1")
    for i in range(0, len1):
        await ctx.send(f"\n- {members[i]}\n")

    await ctx.send("TEAM 2")
    for i in range(len1, len(members)):
        await ctx.send(f"\n- {members[i]}\n")
    
webserver.keep_alive()
bot.run(DISCORD_TOKEN)



