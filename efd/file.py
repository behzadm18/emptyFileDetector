"""
folder.py
-------

This module contains the File class that represents the file checked
by the program to see if they are empty.
"""

__author__ = "Behzad"

import os
import warnings
from typing import Optional, cast


class File():
    """This class represents the files which are checked for being empty.

    :ivar address: address of the file, str
    :ivar justReport: flag to only report empty files. If false, the files
    are modified so that they are not empty.
    :ivar autoFill: fill the empty files automatically with text
    """

    def __init__(self, address: str) -> None:
        """Check the file exists and keep the address in instance variable

        :param address: full address of the file"""
        if not os.path.isfile(address):
            raise FileNotFoundError(
                f'The path specified, "{address}", is not a file.')
        self.address: str = address

    def isempty(self) -> bool:
        """Check if file exists and its size is 0 bytes

        :return: True if the file is empty"""
        return os.path.getsize(self.address) == 0

    def fill(self, text: str = "") -> None:
        """File the empty file with given string or default value

        :param text: the string to be written to the file. If not given, it
        tries to recognize what type of file it is and place commenting
        characters in the file. If the type in not known, a space
        between two quotation marks is written to the file."""
        if not self.isempty():  # make sure the file is empty
            warnings.warn(f'''The file "{self.address}": is not empty and
            is left untouched.''')
            return
        if text is "":
            # commenting characters for some known files
            commenting_chars = {'ini': ';', 'c': '//', 'm': '%',
                                'py': '#', 'java': '//'}
            split_file_address = self.address.split('.')
            # if the file type is not known, write " " to file
            text = commenting_chars.get(split_file_address[-1].lower(), '" "')
        with open(self.address, 'w') as file:
            file.write(text)
