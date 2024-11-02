name = "hello"
description = "bot says hello"

from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello! I am your bot!')


# Setup function to load the cog
async def setup(bot):
    await bot.add_cog(Hello(bot))