import discord
from discord.ext import commands
from discord.ext import *
import pyautogui as pag

intents = discord.Intents.default()

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())

TOKEN = "Get the fuck out"

limit_pixels = 201

def move(direction, px : int, speed : float):
    x = pag.position()[0]
    y = pag.position()[1]

    if (direction == "left"):
        pag.moveTo(x - px, y, speed)
    elif (direction == "right"):
        pag.moveTo(x + px, y, speed)
    elif (direction == "top"):
        pag.moveTo(x, y - px, speed)
    elif (direction == "bottom"):
        pag.moveTo(x, y + px, speed)

@client.event
async def on_ready():
    print("BOT IS READY!")

@client.command()
async def left(ctx, px : int and float):
    if (px < limit_pixels):
        await ctx.send(f"Cursor move to left on {px} pixels")

        move("left", px, 0.5)
    else:
        await ctx.send("Max of pixels - 100")

@client.command()
async def right(ctx, px : int and float):
    if (px < limit_pixels):
        await ctx.send(f"Cursor move to right on {px} pixels")

        move("right", px, 0.5)
    else:
        await ctx.send("Max of pixels - 100")

@client.command()
async def top(ctx, px : int and float):
    if (px < limit_pixels):
        await ctx.send(f"Cursor move to top on {px} pixels")

        move("top", px, 0.5)
    else:
        await ctx.send("Max of pixels - 100")

@client.command()
async def bottom(ctx, px : int and float):
    if (px < limit_pixels):
        await ctx.send(f"Cursor move to bottom on {px} pixels")

        move("bottom", px, 0.5)
    else:
        await ctx.send("Max of pixels - 100")

@client.command()
async def click(ctx):
    await ctx.send("click is completed")
    pag.click()

@client.command()
async def input(ctx, *words):
    await ctx.send("input...")
    sentence = ""

    for i in range(len(words)):
        sentence += words[i] + " "

    pag.write(sentence)

@client.command()
async def enter(ctx):
    await ctx.send("entered")
    pag.press('enter')


client.run(TOKEN)
