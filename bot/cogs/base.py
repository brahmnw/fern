import discord
from discord.ext import commands

class Base(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(aliases=['info','invite'])
    async def help(self, ctx) -> None:

        """Returns bot information."""

        emb = discord.Embed(
            title='fern',
            description='hey im fern!\n[invite me!](https://discord.com/oauth2/authorize?client_id=992708824727293952&permissions=8&scope=bot)\n[my discord!](https://discord.gg/QN4KfD4zsc)',
            color=discord.Colour.from_rgb(255, 74, 119)) \
            .set_thumbnail(url='https://i.imgur.com/CBOUxev.jpeg') \
            .add_field(name="guilds", value=f"{len(self.bot.guilds)}") \
            .add_field(name="prefix", value="-.") \
            .add_field(name="developer", value="brahm") \
            .set_footer(text=f'bot user id: {self.bot.user.id}')
        
        await ctx.send(embed=emb)


async def setup(bot):
    await bot.add_cog(Base(bot))
