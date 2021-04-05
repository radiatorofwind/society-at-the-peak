import discord
from discord.ext import commands
from discord.ext.commands import Cog
import prsaw
import json
from prsaw import RandomStuff
import os
rs = RandomStuff()
config = os.path.abspath('./config.json')
with open(str(config),"r") as cfg:
    cont = cfg.read()
    jso = json.loads(cont)
    prefix = jso["prefix"]
client = commands.Bot(command_prefix=prefix)
class SimpleChat(commands.Cog):
    def __init__(self,client):
        self.client = client
        print("SimpleChat loaded.")
        global dumboenabled
        dumboenabled = False
    @commands.command(name="dumbo",description="Talk to STTP. He's kind of a dumbo, though")
    @commands.has_guild_permissions(administrator=True)
    async def dumbo(self,ctx):
        global dumboenabled
        if dumboenabled:
            dumboenabled = False
            await ctx.send("Dumbo Mode was turned off.")
        elif not dumboenabled:
            dumboenabled = True
            await ctx.send("Dumbo Mode was turned on.")
        else:
            print("!=!=! Dumbo Mode is a value that isn't true nor false. Please fix. !=!=!")
    @commands.Cog.listener()
    async def on_message(self,message):
        global dumboenabled
        if message.author == self.client.user:
            return
        if dumboenabled == True:
            response = rs.get_ai_response(message.content)
            await message.channel.send(response)
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(f"Sorry, but there was an error: {error}")
def setup(client):
    client.add_cog(SimpleChat(client))
