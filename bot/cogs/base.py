import discord
from discord.ext import commands

class Base(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['info','invite','support'])
    async def help(self, ctx):
        embed = discord.Embed(
            title='(น้องบราห์ม) Nong Brahm',
            description='hello i am brahms minion i can do a 540 jump off of the high diving board at ymca\n[Invite Nong Brahm!](https://discord.com/oauth2/authorize?client_id=992708824727293952&permissions=8&scope=bot)',
            color=discord.Colour.from_rgb(255, 74, 119)
        ) \
            .set_thumbnail(url='https://i.imgur.com/bmmFpaf.jpg') \
            .add_field(name="Links", value="""
[Wiki](https://github.com/MrBrahm/nongbrahm/wiki)
[Commands](https://github.com/MrBrahm/nongbrahm/wiki/Commands)
[Github](https://github.com/MrBrahm/nongbrahm)
[Support Server](https://discord.gg/QN4KfD4zsc)
            """) \
            .add_field(name="Servers", value=f"{len(self.bot.guilds)}") \
            .add_field(name="Credits", value="Made by Brahm#8516") \
            .set_footer(text=f'ID: {self.bot.user.id}')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Base(bot))
