import discord
from json import loads
from decimal import Decimal as d

bot = discord.Bot()
token = 'PUT TOKEN HERE'

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Retime Bot | Made by Conner#4200'))
    print(f'{bot.user.name} is ready!')

def format(time):
    time = str(time)
    time = time.split('.', 1)
    seconds = int(time[0])
    milliseconds = str(time[1])
    minutes = seconds//60
    hours = minutes//60
    if seconds > 60 or seconds == 60:
        seconds = seconds - (minutes * 60)
    if minutes > 60 or minutes == 60:
        minutes = minutes - (hours * 60)
    if seconds == '0':
        return (f'0s {milliseconds}ms')
    elif minutes == '0':
        if len(seconds) == 1:
            return (f'0{str(seconds)}s {milliseconds}ms')
        else:
            return (f'{str(seconds)}s {milliseconds}ms')
    elif hours == '0':
        return (f'{str(minutes)}m {str(seconds)}s {milliseconds}ms')
    else:
        return (f'{str(hours)}h {str(minutes)}m {str(seconds)}s {milliseconds}ms')

@bot.slash_command(name = 'frame', description = 'Retime with the Frame')
async def frame(ctx, start: discord.Option(int, "Start Time",), end: discord.Option(int, "End Time"), framerate: discord.Option(int, "Framerate")):
    try:
        time = str(round((end - start) / framerate, 3))
    except:
        await ctx.respond('Error: An Unkown Error Occured', ephemeral = True)
    try:
        formatted_time = format(time)
    except:
        await ctx.respond('Error: An Unkown Error Occured', ephemeral = True)
    embed = discord.Embed(
        title = 'Final Time', 
        description = f'Your Final time is: {formatted_time}',
        color = 0x00ff00)
    await ctx.respond(embed = embed, ephemeral = True)

@bot.slash_command(name = 'debug_info', description = 'Retime with the Debug Info')
async def debug_info(ctx, start: discord.Option(str, "Start Time",), end: discord.Option(str, "End Time"), framerate: discord.Option(int, "Framerate")):
    try:
        start_dict = loads(start)
    except:
        await ctx.respond('Error: Invalid Start Debug Info', ephemeral = True)
        return
    try:
        end_dict = loads(end)
    except:
        await ctx.respond('Error: Invalid End Debug Info', ephemeral = True)
        return
    try:
        start_cmt = d(start_dict['cmt'])
    except:
        await ctx.respond('Error: Invalid Start Debug Info', ephemeral = True)
        return
    try:
        end_cmt = d(end_dict['cmt'])
    except:
        await ctx.respond('Error: Invalid End Debug Info', ephemeral = True)
        return
    try:
        framerate = int(framerate)
    except:
        await ctx.respond('Error: Invalid Framerate', ephemeral = True)
    try:
        time = str(round((d(end_cmt) - d(start_cmt)) - (d(end_cmt) - d(start_cmt)) % (d(1)/int(framerate)), 3))
    except:
        await ctx.respond('Error: An Unkown Error Occured', ephemeral = True)
        print('Alert: An Unkown Error Occured')
    try:
        formatted_time = format(time)
    except:
        await ctx.respond('Error: An Unkown Error Occured', ephemeral = True)
    embed = discord.Embed(
        title = 'Final Time', 
        description = f'Your Final time is: {formatted_time}',
        color = 0x00ff00)
    await ctx.respond(embed = embed, ephemeral = True)
    
bot.run(token)