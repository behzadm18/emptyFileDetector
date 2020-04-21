"""
folder.py
-------

This module contains the Folder class that represents the folder inside
which the program looks for empty files.
"""

__author__ = "Behzad"


import os

from typing import Set


class Folder(object):
    """This class represents the folder containing the file to be checked by
    :meth: `efd.File.isempty` recursively.

    :ivar address: address of the folder
    """
    def __init__(self, address: str) -> None:
        """Check if the the folder path exists and keep in instance variable"""
        if not os.path.isdir(address):
            raise FileNotFoundError(
                f'The path specified, "{address}", is not a folder.')
        self.address: str = address

    def all_files(self) -> Set[str]:
        """Find all files in the folder recursively and return as a set"""
        file_set: Set[str] = set()
        for root, _, files in os.walk(self.address):
            for file in files:
                file_set.add(os.path.join(root, file))
        return file_set


# folder = Folder(r"C:\Program Files\7-Zip")
# print(folder.all_files())
