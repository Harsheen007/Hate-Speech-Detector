import discord
import pandas as pd
import asyncio
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GENERATOR_BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Load Dataset
df = pd.read_csv("Dynamically Generated Hate Dataset v0.2.2.csv")  # Replace with your dataset filename

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        for index, row in df.iterrows():
            await channel.send(row["text"])  # Adjust column name
            await asyncio.sleep(60)  # Wait 1 minute before posting next message

bot.run(TOKEN)