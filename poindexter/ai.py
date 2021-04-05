import discord
from discord.ext import commands
from prsaw import RandomStuff

bot = commands.Bot(command_prefix=">")
rs = RandomStuff(async_mode = True)

token = "ODI2NTYzODA1NzE4NTExNjM2.YGOTiA.26hu-M644kZNJ0MU4PwDZxLtAN8"

@bot.event
async def on_message(message):
    if bot.user == message.author:
        return
    if message.channel.id == 826562236516007956 or 826589060780785715 or 821980072939356170:
        response = await rs.get_ai_response(message.content)
        await message.channel.send(response)
    await bot.process_commands(message)

bot.run(token)