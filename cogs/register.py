import discord
from discord.ext import commands
import os
import json

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='register', help='Prints the user ID of the author')
    async def register(self, ctx):
        user_id = ctx.author.id
        username = ctx.author.name

     #   Check if the "users" folder exists, if not, create it
        if not os.path.exists('./users'):
            os.makedirs('./users')
            # print("Created 'user' folder")
        # else:
            # print('"users" folder already exists!')
        
        # path for the users file
        file_path = f'./users/{user_id}.json'

        # Check if the JSON file exists, if not, create it
        if not os.path.exists(file_path):
            # Create the JSON file and add user_id and username to it
            user_data = {
                'user_id': user_id,
                'username': username,
                'balls': 500
            }
            with open(file_path, 'w') as f:
                json.dump(user_data, f, indent=4)
            print(f'User {username} with ID {user_id} has been registered')
        else:
            print(f'User {username} with ID {user_id} is already registered')

        print(f'User {username}\'s ID is {user_id}')
        await ctx.send(f'User {username}\'s ID is {user_id}')

async def setup(bot):
    await bot.add_cog(Register(bot))