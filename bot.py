import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the token from the .env file
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN is None:
    raise ValueError("No DISCORD_TOKEN found in environment variables")


# Intents setup (required to handle certain bot activities)
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read message content

# Define the prefix 


# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

async def main():
    async with bot:
        # Load all the commands from the cogs folder
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}') # Removes the .py from the filename
        
        # load the custom command cog from the cog folder

        await bot.start(TOKEN)


# Run the bot with your token
asyncio.run(main())
