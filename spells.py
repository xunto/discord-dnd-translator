import csv
from typing import List, Tuple


class TermsRepository:
    @staticmethod
    def __read_spells_csv(filename) -> List[Tuple[str, ...]]:
        """
        """
        dictionary = []
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                dictionary.append(tuple(row))
        return dictionary

    @staticmethod
    def __normalize_name(string: str) -> str:
        return string \
            .lower() \
            .strip() \
            .replace('`', '\'') \
            .replace('’', '\'')

    def __init__(self):
        self.dictionary = TermsRepository.__read_spells_csv('spells.csv')

    async def translate_spell_name(self, spell_name):
        spell_normalized = TermsRepository.__normalize_name(spell_name)
        for aliases in self.dictionary:
            if spell_normalized in map(
                    TermsRepository.__normalize_name,
                    aliases):
                return aliases
        return None
