# Pycord Docs : https://guide.pycord.dev/interactions/application-commands/slash-commands
# reference : https://stackoverflow.com/questions/71165431/how-do-i-make-a-working-slash-command-in-discord-py

from discord.ext import commands
import webbrowser

bot = commands.Bot()
lock = False

@bot.slash_command(name="lock") 
async def lock(ctx): 
    global lock

    if not lock:
        webbrowser.open('http://192.168.1.55/26/off')
        print('browser opened')
        await ctx.respond("Door is now locked!")
    else:
        print('browser opened')
        await ctx.respond("Door is already locked!")

    lock = True
    
@bot.slash_command(name="unlock") 
async def unlock(ctx): 
    global lock

    if not lock:
        await ctx.respond("Door is already unlocked!")
    else:
        webbrowser.open('http://192.168.1.55/26/on')
        await ctx.respond("Door is now unlocked!")

    lock = False

bot.run("MTEzOTM4NTQyMjM5MzM4NDk2MA.GOGVuO.UglpLZMjDa_gfM3RbyoTBCWBSeYywZsarxXJk8")