import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def embed(ctx, titulo: str, descricao: str, url_imagem: str):
    embed = discord.Embed(title=titulo, description=descricao, color=0x00ff00)
    embed.set_image(url=url_imagem)
    await ctx.send(embed=embed)

bot.run('MTM4ODcxNzE0NTIzOTg0NjkxMg.GzWDlP.62PWsZJ2PDv2kK03-3FjbK7WisfLGOg2nrButA')
