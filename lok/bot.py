from discord.ext import commands

bot = commands.Bot()

@bot.command(description="Sends the bot's latency.")
async def ping(ctx):
    await ctx.send(f"Pong! Latency is {round(bot.latency * 1000)}ms")

# Pycord Docs : https://guide.pycord.dev/interactions/application-commands/slash-commands
# reference : https://stackoverflow.com/questions/71165431/how-do-i-make-a-working-slash-command-in-discord-py
@bot.slash_command(name="first_slash", guild_ids=[...]) # Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")

bot.run("dont leak this :D")