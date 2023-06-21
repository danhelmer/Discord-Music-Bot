import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?',intents=intents)
#import all of the cogs
bot.remove_command('help')
from help_cog import help_cog
from music_cog import music_cog
@bot.event
async def on_ready():
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))
#remove the default help command so that we can write out own

bot.run(os.getenv('TOKEN'))