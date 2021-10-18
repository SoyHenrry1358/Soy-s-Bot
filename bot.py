import discord
from discord import channel
from discord import message
from discord.embeds import Embed
from discord.ext import commands
import random 
import json
import os
import time
import asyncio

bot = commands.Bot(command_prefix='s!')

with open('setting.json', 'r', encoding='utf-8') as jfile:
    jdata=json.load(jfile)

@bot.event
async def on_ready():
    print("Your Bot Is Online Do Not Turn Off Your Computer")

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='s!help'))

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="指令说明", description="** **", color=0xffff8a)
    embed.set_author(name="FbBot", icon_url="https://cdn.discordapp.com/attachments/881417611374649356/899628886382510100/avatar.png")
    embed.add_field(name="Ping", value="`检测机器人延迟` \n\n**   **")
    embed.add_field(name="Server", value="`获得官方服务器连接` \n\n**   **")
    embed.add_field(name="Omlet", value="`获得开发者Omlet Arcade连接` \n\n**   **")
    embed.add_field(name="Coin", value="`投掷硬币` \n\n**   **")
    embed.add_field(name="Ask", value="`问机器人一个问题` \n\n**   **")
    embed.add_field(name="Sus", value="`获得一张Sus图` \n\n**   **")
    embed.add_field(name="RickRoll", value="`获得一张RickRoll动图` \n\n**   **")
    embed.add_field(name="Roulette", value="`俄罗斯左轮手枪` \n\n**   **")
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong!", color=0xffff8a)
    embed.add_field(name=f":hourglass:Time: {round(bot.latency)} ms", value="** **")
    await ctx.send(embed=embed)

@bot.command()
async def server(ctx):
    await ctx.send(f"**凋哥dc群欢迎~**https://discord.gg/9ET2mDzMPC")

@bot.command()
async def dice(ctx):
    dice_number=["1", "2", "3", "4", "5", "6"]
    await ctx.send(f"你掷出了 **{random.choice(dice_number)}** 点！")

@bot.command()
async def omlet(ctx):
    await ctx.send(f"https://omlet.gg/profile/soyhenrry1358")

@bot.command()
async def ask(ctx):
    answer=["是", "不是", "或许是", "或许不是", "不知道", "\:D"]
    await ctx.send(f"{random.choice(answer)}")

@bot.command()
async def sus(ctx):
    await ctx.send(f"https://yt3.ggpht.com/99pYdn7oVmH3r5iCyPXKwhntvYNNnODSJjTRyyxdexcmKSjGoELGa0cG_gEAHV-WWa_Xb4tF5A=s900-c-k-c0x00ffffff-no-rj")

@bot.command()
async def rickroll(ctx):
    await ctx.send(f"https://c.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif")

@bot.command()
async def roulette(ctx):
    r = {random.choice(jdata['roulette'])}
    a = (jdata['a'])
    b = (jdata['b'])
    c = (jdata['c'])
    d = (jdata['d'])
    e = (jdata['e'])
    f = (jdata['f'])
    g = (jdata['g'])
    h = (jdata['h'])
    await ctx.send (f"**稍等片刻.....**")
    time.sleep(2.5)
    
    
    if r == {'a'}:
        await ctx.send(f"**{random.choice(a)}**")
    elif r == {'b'}:
        await ctx.send(f"**{random.choice(b)}**")
    elif r == {'c'}:
        await ctx.send(f"**{random.choice(c)}**")
    elif r == {'d'}:
        await ctx.send(f"**{random.choice(d)}**")
    elif r == {'e'}:
        await ctx.send(f"**{random.choice(e)}**")
    elif r == {'f'}:
        await ctx.send(f"**{random.choice(f)}**")
    elif r == {'g'}:
        await ctx.send(f"**{random.choice(g)}**")
    else:
        await ctx.send(f"**{random.choice(h)}**")

@bot.event
async def on_message(msg):
    oao = (f"{random.choice(jdata['oao'])}")
    if msg.content == "oao" and msg.author != bot.user:
        await msg.channel.send(oao)

@bot.event
async def on_message(msg):
    m = (jdata['mouse'])
    if msg.content == "有老鼠" and msg.author !=bot.user:
        await msg.channel.send(f"**机器喵启动中....**")
        time.sleep(2.5)
        await msg.channel.send(f"**发现目标**")
        time.sleep(4)
        await msg.channel.send(m)
        time.sleep(2.5)
        await msg.channel.send(f"**喵喵队立大功(◍°∇°◍)ﾉ**")


bot.run(jdata['token'])