from symbol import except_clause
import discord
from json import loads
from decimal import Decimal as d

bot = discord.Bot()
token = 'PUT TOKEN HERE'

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

def format(time):
    time = str(time)
    time = time.split('.', 1)
    seconds = int(time[0])
    milliseconds = str(time[1])
    minutes = seconds//60
    hours = minutes//60
    if seconds > 60:
        seconds = seconds - (minutes * 60)
    if minutes > 60:
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
    formatted_time = format(d(round((end - start) / framerate, 3)))
    await ctx.respond(f'Your Final Time is: {formatted_time}')

@bot.slash_command(name = 'debug_info', description = 'Retime with the Debug Info')
async def debug_info(ctx, start: discord.Option(str, "Start Time",), end: discord.Option(str, "End Time"), framerate: discord.Option(int, "Framerate")):
    try:
        start_dict = loads(start)
    except:
        await ctx.respond('Error: Invalid Start Debug Info')
        return
    try:
        end_dict = loads(end)
    except:
        await ctx.respond('Error: Invalid End Debug Info')
        return
    try:
        start_cmt = d(start_dict['cmt'])
    except:
        await ctx.respond('Error: Invalid Start Debug Info')
        return
    try:
        end_cmt = d(end_dict['cmt'])
    except:
        await ctx.respond('Error: Invalid End Debug Info')
        return
    try:
        framerate = int(framerate)
    except:
        await ctx.respond('Error: Invalid Framerate')
    formatted_time = format(d(round(end_cmt - start_cmt) - (end_cmt - start_cmt) % (d(1)/framerate), 3))
    await ctx.respond(f'Your Final Time is: {formatted_time}')
    
    
bot.run(token)