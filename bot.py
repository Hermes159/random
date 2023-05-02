
##import os
from discord.ext import commands
import discord
from discord import app_commands



##intents = discord.Intents.default()
##client = discord.Client(intents=intents)
##tree = app_commands.CommandTree(client)



BOT_TOKEN = "########################################################################"
CHANNEL_ID = ###################
             

bot = commands.Bot(command_prefix="&", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Boas, o Tiburcio esta pronto!!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Boas, Tibúrcio o Gnomo da Floresta esta ONLINE!!")


@bot.command()
async def tiburcio(ctx):
    await ctx.send(f"Boas! {ctx.message.author.mention}")

@bot.command()
async def ajuda(ctx):
    await ctx.send("""
Comandos disponiveis:
-&tiburcio     -&origem
-&enigma       -&calculadora 
-&resposta
""")


    
@bot.command()
async def enigma(ctx):
    await ctx.send("If You Look At The Numbers On My Face, You Won't Find 13 Anyplace. What am I?")
    

@bot.command()
async def resposta(ctx,*, args):
##    x = args    
    if args == "clock":
        await ctx.send(f"Boa! {ctx.message.author.mention}")
                
    else:
        await ctx.send(f"Epah {ctx.message.author.mention} das duas uma ou es burro que doi ou escreveste mal")






@bot.command()
async def origem(ctx):
    await ctx.send("""
Tibrúcio, também conhecido por Gnomo da Floresta é um ser místico proveniente de florestas.
Tibúrcio representa paz, calma, serenidade e bonança.
Sendo considerado por muitos um sinal de sorte e prosperidade!
""")
    await ctx.send("https://tenor.com/b0hQy.gif")
 

@bot.command()
async def calculadora(ctx,x:int,arg,y:int):
    if arg == "/":
        d = x/y
        await ctx.send(f"{d}")
    if arg == "*":
        m = x*y
        await ctx.send(f"{m}")
    if arg == "-":
        dd = x-y
        await ctx.send(f"{dd}")
    if arg == "+":
        s = x+y
        await ctx.send(f"{s}")
    


    
   


   

   

##@bot.tree.command(name="cenoura")
##async def cenoura(interaction: discord.Interaction):
##    await interaction.response.send_message(f"Boas {interaction.user.mention} encontras-te um easter egg!!"
##    ephemeral=True)
    




bot.run(BOT_TOKEN)
