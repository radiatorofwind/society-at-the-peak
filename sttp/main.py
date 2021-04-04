import discord
from discord.ext import commands, tasks
from discord.ext.commands import Cog
from discord_slash import SlashCommand, SlashContext
import asyncio
import json
with open("config.json","r") as cfg:
    cont = cfg.read()
    jso = json.loads(cont)
    token = jso["token"]
    prefix = jso["prefix"]
extensions = ["cogs.simplechat"]
client = commands.Bot(command_prefix=prefix)
# On ready
@client.event
async def on_ready():
    print("Society is at it's peak. All going down from here.")
@client.command(name="reload",description="Reloads extension.")
async def reload(ctx,content):
    if not content in extensions:
        await ctx.send(f"Extension not found. Here are a list of extensions:\n{extensions}")
    else:
        await ctx.send(f"Reloading extension {content}...")
        client.reload_extension(content)
if __name__ == "__main__":
    for extension in extensions:
        client.load_extension(extension)
else:
    print("Please run the program directly.")
client.run(token)
