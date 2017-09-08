import os
import csv
from typing import Union, Tuple

from whoosh import index, fields, query


class DictionaryRecord(fields.SchemaClass):
    group = fields.NUMERIC(stored=True)
    content = fields.TEXT(stored=True)


class Dictionary:
    """
    Responsible for fetch and search of translations.
    """
    INDEX_PATH = ".index"

    def __update_index(self, data) -> None:
        """
        Update index with specified data.
        :param data: Data.
        :return: Nothing.
        """
        writer = self.index.writer()
        for i, row in enumerate(data):
            for variant in row:
                writer.add_document(
                    group=i,
                    content=variant
                )
        writer.commit()

    def __init_index(self):
        # TODO: Add a way to clear index
        # if os.path.exists(index_dir):
        #     self.index = index.open_dir
        # else:
        #    os.mkdir(index_dir)
        self.index = index.create_in(Dictionary.INDEX_PATH, DictionaryRecord)

    def __init__(self, data):
        self.__init_index()
        self.__update_index(data)

    @classmethod
    def from_csv_file(cls, filename: str):
        """
        Create dictionary from csv file.
        :param filename: CSV file name.
        :return: Dictionary object.
        """
        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            return cls(reader)

    async def translate_spell_name(self, spell_name: str) -> Union[
            None,
            Tuple[str, ...]]:
        """
        Translate spell_name and return all translations.
        :param spell_name: Spell name.
        :return: List of translations.
        """
        with self.index.searcher() as searcher:
            # TODO: query is not working
            result = searcher.search(
                query.Term("content", spell_name)
            )
            print(list(result))
        return None
