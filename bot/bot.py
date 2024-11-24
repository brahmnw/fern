import discord
from discord.ext import commands
import json
import aiohttp
import asyncio

class Fern(commands.Bot):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    async def start(self, *args, **kwargs) -> None:

        """base code to run prior to starting the bot. starts an aiohttp ClientSession() for interaction with webAPIs."""

        self.session = aiohttp.ClientSession()
        await super().start(*args, **kwargs)

    async def close(self, *args, **kwargs) -> None:

        """base code to run when properly closing the bot. starts an aiohttp ClientSession() for interaction with webAPIs."""

        await self.session.close()
        await super().close()

loadup_cogs = [
    'base',
    'events',
    'owner'
]

intents = discord.Intents.all()
bot = Fern(
    intents=intents,
    command_prefix='-.',
    owner_ids=[
        154433538375024640
    ]
)

# remove unnecessary commands
bot.remove_command('help')


async def main(client) -> None:

    # load the startup cogs
    for cog in loadup_cogs:
        await client.load_extension(f"cogs.{cog}")

    # load discord bot info
    with open('info.json', 'r') as f:
        client_info = json.loads(f.read())

    client.info = client_info

    await client.start(client_info['tokens']['discord'])


if __name__ == '__main__':

    asyncio.run(main(bot))
