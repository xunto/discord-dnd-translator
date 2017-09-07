import csv
from typing import Union, List, Tuple


class Dictionary:
    """
    Responsible for fetch and search of translations.
    """

    @staticmethod
    def __read_spells_csv(filename) -> List[Tuple[str, ...]]:
        """
        Read spell names from specified file.
        :param filename: Filename.
        :return: List of names and translations.
        """
        dictionary = []
        with open(filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                dictionary.append(tuple(row))
        return dictionary

    @staticmethod
    def normalize_name(string: str) -> str:
        """
        Normalize string.
        :param string: Some string.
        :return: Normalized string.
        """
        return string \
            .lower() \
            .strip() \
            .replace('`', '\'') \
            .replace('’', '\'')

    def __init__(self):
        self.dictionary = Dictionary.__read_spells_csv('spells.csv')

    async def translate_spell_name(self, spell_name: str) -> Union[
            None,
            Tuple[str, ...]]:
        """
        Translate spell_name and return all translations.
        :param spell_name: Spell name.
        :return: List of translations.
        """
        spell_normalized = Dictionary.normalize_name(spell_name)
        for aliases in self.dictionary:
            if spell_normalized in map(
                    Dictionary.normalize_name,
                    aliases):
                return aliases
        return None
