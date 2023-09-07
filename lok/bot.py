from discord.ext import commands

bot = commands.Bot()

@bot.slash_command(name="lock") 
async def lock(ctx): 
    await ctx.respond("Door is now locked!")

@bot.slash_command(name="unlock") 
async def unlock(ctx): 
    await ctx.respond("Door is now unlocked!")

bot.run("MTEzOTM4NTQyMjM5MzM4NDk2MA.GOGVuO.UglpLZMjDa_gfM3RbyoTBCWBSeYywZsarxXJk8")