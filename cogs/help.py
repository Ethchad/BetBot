import discord
from discord.ext import commands
import os


# This defines a class that inherits from commands.Cog, which is a base class for creating cogs in discord.py
class ListCommands(commands.Cog):
    def __init__(self, bot):
        # Initializes the cog with a reference ot the bot instance
        self.bot = bot


    # defines a command that lists all commands in the cogs folder with their descriptions
    @commands.command(name='listcommands', help='Lists all commands in the cogs folder with their descriptions')
    async def list_commands(self, ctx):
        # Initialize an empty list to store the command names and descriptions
        command_list = []

        # iterate over all files in the 'cogs' directory
        for filename in os.listdir('./cogs'):
            # Check if the file is a Python file
            if filename.endswith('.py'):
                # Remove the '.py' extension from the filename to get the cog name
                cog_name = filename[:-3]
                try:
                    # Load the cog dynamically using the cog name
                    self.bot.load_extension(f'cogs.{cog_name}')
                    # Iterate over all the commands and its help descriptions to the command list
                    for command in self.bot.get_cog(cog_name).get_commands():
                        # append the command name and its help description to the command list
                        command_list.append(f'{command.name}: {command.help}')
                except Exception as e:
                    # Print an error message if the cog fails to load
                    print(f'Failed to load cog {cog_name}: {e}')
        
        # Create an embed to display the commands
        embed = discord.Embed(title="List of Commands", color=discord.Color.blue())


        # check if any commands where found
        if command_list:
            # add each command as a field in the embed
            for name, help_text in command_list:
                embed.add_field(name=name, value = help_text, inline=False)
            
            # send the list of commands to the discord channel
            # await ctx.send('\n'.join(command_list))
        else:
            # add a field indicating that no commands were found
            embed.add_field(name='No commands found', value="There are no cammands in the cogs folder", inline=False)

            # Send a message indicating that no commadns were found
            # await ctx.send('No commands found in the cogs.')
        # send the embed to the discord channel
        await ctx.send(embed=embed)

# Defines an asynchronous setup function to add the cog to the bot
async def setup(bot):
    # Add the ListCommands cog to the bot

    await bot.add_cog(ListCommands(bot)) 