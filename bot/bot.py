import discord
from discord.ext import commands
import json
import aiohttp
import asyncio

class NongBrahm(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def start(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()
        await super().start(*args, **kwargs)

    async def close(self, *args, **kwargs):
        await self.session.close()
        await super().close()

loadup_cogs = [
    'base',
    'events',
    'owner'
]

intents = discord.Intents.all()
bot = NongBrahm(
    intents=intents,
    command_prefix='>>',
    owner_ids=[
        154433538375024640
    ]
)

bot.remove_command('help')


async def main(client):

    for cog in loadup_cogs:
        await client.load_extension(f"cogs.{cog}")

    with open('tokens.json', 'r') as f:
        client_info = json.loads(f.read())

    client.info = client_info

    await client.start(client_info['token'])


if __name__ == '__main__':

    asyncio.run(main(bot))
