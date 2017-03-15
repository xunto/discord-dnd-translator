import csv

dictionary = []


def read_spells_csv():
    with open('spells.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for russian, english in reader:
            dictionary.append((russian, english))


read_spells_csv()


def normalize_name(string):
    return string \
        .lower() \
        .strip() \
        .replace('`', '\'') \
        .replace('’', '\'')


async def translate_spell_name(spell):
    spell_normalized = normalize_name(spell)
    for russian, english in dictionary:
        if normalize_name(russian) == spell_normalized:
            return russian, english
        elif normalize_name(english) == spell_normalized:
            return english, russian
    return spell, "Не найдено"
