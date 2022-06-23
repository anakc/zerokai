import discord
from discord.ext import commands

client = commands.Bot( command_prefix = '.', intents = discord.Intents.all() )
# .help

@client.event

async def on_ready():
    print( 'Бот подключился на сервер')

@client.command( pass_context = True )

async def hello( ctx ):
    await ctx.send( 'Hello. Я бот дискорда' ) 
    
    # Connect

    token = open( 'token.txt', 'r').readline()

client.run( token )