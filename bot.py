

from discord.ext import commands
import discord




BOT_TOKEN = "########################################################################################"
CHANNEL_ID = ###################
             

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
