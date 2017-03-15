import os

import discord

import spells

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as', client.user.name)


@client.event
async def on_message(message):
    content = message.content
    if content.startswith('!spell'):
        _, spell = content.split(' ', maxsplit=1)
        spell, translation = await spells.translate_spell_name(spell)
        await client.send_message(message.channel, f"{spell}: {translation}")


client.run(os.environ['DISCORD_CLIENT_KEY'])
