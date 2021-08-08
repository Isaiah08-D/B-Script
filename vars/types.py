import os
import sys


class String(str):
    def __init__(self, value=str):
        """
        Creates a string
        :param value:
        """
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
        self.value = value

    def _repr__(self):
        return self.value

    def __str__(self, inbetween=''):
        """
        Puts the list together into a string.
        :param inbetween: what is inbetween the items in the list. Defaults to an empty string.
        :return:
        """
        return inbetween.join(self.value)

    def __list__(self):
        """
        Returns the list.
        :return:
        """
        return self.value

    def __len__(self):
        return len(self.value)

    def __type__(self):
        return 'list'
