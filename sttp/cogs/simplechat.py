import discord
from discord.ext import commands
from discord.ext.commands import Cog
client = commands.Bot(command_prefix="sttp")
class SimpleChat(commands.Cog):
    def __init__(self,bot):
        print(self)
        self.client = client
    #@commands.command(name="mfinder",description="Locates music.")
    #async def musicfinder()
def setup(bot):
    bot.add_cog(SimpleChat(client))
