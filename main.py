import discord
import os
from dotenv import load_dotenv


# Lade Umgebungsvariablen
load_dotenv()
TOKEN = os.getenv('TOKEN')


# Bot-Konfiguration
intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} ist jetzt online.')
    
# Bot starten und Cogs laden
if __name__ == "__main__":
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"cogs.{filename[:-3]} loading complete")
    
bot.run(TOKEN)    
    
    
    
    
    
    
    
