import discord

from spells import TermsRepository


class DnDTranslator(discord.Client):
    """
    Bot designed to translate some D&D 5e spells and terms.
    """

    def __init__(self):
        super().__init__()
        self.repository = TermsRepository()

    async def on_ready(self):
        """
        Post login initialization.
        """
        print('Logged in as', self.user.name)

    async def handle_spell_translation(self, spell_name):
        """
        Translate spell name.
        """
        aliases = await self.repository.translate_spell_name(spell_name)
        if aliases:
            return '/'.join(sorted(aliases))
        return f"\"{spell_name}\" не найдено :disappointed_relieved:"

    async def on_message(self, message):
        """
        Message handler and command handlers.
        """
        content = message.content

        result_embed = None
        if content.startswith('!spell'):
            _, spell_name = content.split(' ', maxsplit=1)
            result_embed = discord.Embed(title=spell_name[:1].upper() + spell_name[1:].lower(),
                                         description=await self.handle_spell_translation(spell_name),
                                         colour=0xDEADBF)

        if result_embed:
            await self.send_message(message.channel, embed=result_embed)


def main():
    """
    Init bot class and start it.
    Takes client key from ENV "DISCORD_CLIENT_KEY".
    """

    # DnDTranslator().run(os.environ['DISCORD_CLIENT_KEY'])
    DnDTranslator().run('MzUyNTY4NjM3Njk0OTM1MDUw.DIjCpg.OQ-cGG_pqRpi5Ut-FiEjnDjI-hI')


if __name__ == '__main__':
    main()
