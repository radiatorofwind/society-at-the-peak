import discord
import json
from discord.ext import commands
from prsaw import RandomStuff
with open("config.json","r") as file:
    cntnt = file.read()
    jso = json.loads(cntnt)
    token = jso["token"]
bot = commands.Bot(command_prefix=">")
rs = RandomStuff(async_mode = True)
@bot.event
async def on_message(message):
    if bot.user == message.author:
        return
    if message.channel.id == 826562236516007956 or 826589060780785715 or 821980072939356170:
        response = await rs.get_ai_response(message.content)
        await message.channel.send(response)
    await bot.process_commands(message)
bot.run(token)
