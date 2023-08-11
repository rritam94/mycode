from discord.ext import commands

bot = commands.Bot()

@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.send(f"Pong! Latency is {round(bot.latency * 1000)}ms")

bot.run('MTEzOTM4NTQyMjM5MzM4NDk2MA.GpK3IJ.0gp9HdxACSgL9K7UwehyGm_Mmc1wD8-VDUPBmA')