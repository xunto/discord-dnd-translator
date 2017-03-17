import csv

dictionary = []


def read_spells_csv():
    with open('spells.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            dictionary.append(row)


read_spells_csv()


def normalize_name(string):
    return string \
        .lower() \
        .strip() \
        .replace('`', '\'') \
        .replace('’', '\'')


async def translate_spell_name(spell):
    spell_normalized = normalize_name(spell)
    for aliases in dictionary:
        if spell_normalized in map(normalize_name, aliases):
            return aliases
    return None
