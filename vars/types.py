import os
import sys


def __type__():
    return 'string'


class String(str):
    def __init__(self, value=str):
        """
        Creates a string
        :param value:
        """

        self.type = 'string'
        self.value = str(value)

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value

    def __list__(self, char=' '):
        """
        Returns the string in list format.
        :param char: what to split the string by
        :return:
        """
        return self.value.split(char).strip("'").strip('"')

    def __len__(self):
        return len(self.value)

    def __type__(self):
        return 'string'


class List:
    def __init__(self, value):
        """
        Creates a list
        :param value: the list to be created
        """
        self.value = []
        self.type = 'list'

        for item in value[1:].split(':'):
            item = item.strip()
            self.value.append(item)

    def _repr__(self):
        return self.value

    def __getitem__(self, item):
        """
        Get an item from the list.
        :param item: Index of the item. Note that B-Script indexing starts with 1.
        :return:
        """
        return self.value[item-1]

    def __str__(self, between=''):
        """
        Puts the list together into a string.
        :param between: what is in-between the items in the list. Defaults to an empty string.
        :return:
        """
        return between.join(self.value)

    def __list__(self):
        """
        Returns the list.
        :return:
        """
        return self.value

    def __len__(self):
        return len(self.value)

