import discord
from discord.ext import commands

class GymBro(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot


async def setup(bot):
    await bot.add_cog(GymBro(bot))