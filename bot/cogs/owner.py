import discord
from discord.ext import commands
import aiohttp
import asyncio
from time import time
import sys
import os

class Owner(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['o'], hidden=True)
    @commands.is_owner()
    async def _owner(self, ctx):
        return

    @_owner.command(aliases=['l'])
    async def _load(self, ctx, module):

        """Loads a cog from bot.cogs"""

        try:
            await self.bot.load_extension(f"cogs.{module}")
        
        except Exception as e:
            print(e)
            await ctx.send(f":hammer: `{module}` could not be successfully reloaded.")

        else:
            await ctx.send(f":hammer: **Reloaded** `{module}`!")

    @_owner.command(aliases=['rl'], hidden=True)
    async def _reload(self, ctx, module):

        """Reloads a cog from bot.cogs"""

        try:
            await self.bot.reload_extension(f"cogs.{module}")
        
        except Exception as e:
            print(e)
            await ctx.send(f":hammer: `{module}` could not be successfully reloaded.")

        else:
            await ctx.send(f":hammer: **Reloaded** `{module}`!")

    @_owner.command(aliases=['ul'], hidden=True)
    async def _unload(self, ctx, module):

        """Unloads a cog from bot.cogs"""

        try:
            await self.bot.unload_extension(f"cogs.{module}")
        
        except Exception as e:
            print(e)
            await ctx.send(f":hammer: `{module}` could not be successfully unloaded.")

        else:
            await ctx.send(f":hammer: **Unloaded** `{module}`!")

    @_owner.command(hidden=True)
    async def _presence(self, ctx, *, presence):

        """Changes the currently playing discord game."""

        await self.bot.change_presence(activity=discord.Game(presence))
        await ctx.send(f"Successfully changed presence to `{presence}`!")

    @_owner.command(aliases=['ss'], hidden=True)
    async def _start_aiohttp(self, ctx):

        """Begins a client session for aiohttp."""

        self.bot.session = aiohttp.ClientSession()
        await ctx.send(f"Started `aiohttp.ClientSession()`.")

    @_owner.command()
    async def list_servers(self, ctx):
        
        """Returns a list of all servers that the bot is in"""

        servers = []
        for s in self.bot.guilds:
            servers.append(s.name)

        await ctx.send('\n'.join(servers))

async def setup(bot):
    await bot.add_cog(Owner(bot))