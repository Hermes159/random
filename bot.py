

from discord.ext import commands
import discord




BOT_TOKEN = "MTA5NDI5MzY1NDI3OTA0MTEzNg.G6iq8L.9avhSorz9YR7wLIBwvtbMAss6UZjHpWaJFzawc"
CHANNEL_ID = 1094294281830801500


bot = commands.Bot(command_prefix="&", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Boas, o Tiburcio esta pronto!!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Boas, Tiburcio o Gnomo da Floresta esta pronto!!")


@bot.command()
async def tiburcio(ctx):
    await ctx.send("Boas!")

bot.run(BOT_TOKEN)
