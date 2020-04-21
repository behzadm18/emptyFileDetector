"""
This files contains the fixtures and constants used by the unit tests

"""

__author__ = "Behzad"

import pytest

FOLDERADDRESS = r'/folder_test'


@pytest.fixture
def fake_file_system(fs):  # pylint: disable=invalid-name
    """Create fake file system

    It has a folder structure with some empty files here and there.
    The first number suffix shows the folder level and the second one is the
    file index in that folder"""
    fs.create_file(FOLDERADDRESS + r'/file00.txt')
    with open(FOLDERADDRESS + r'/file00.txt', 'w') as file:
        file.write('some contents')
    fs.create_file(FOLDERADDRESS + r'/emptyfile01.INI')
    fs.create_file(FOLDERADDRESS + r'/filecontainingspace02.m')
    with open(FOLDERADDRESS + r'/filecontainingspace02.m', 'w') as file:
        file.write(' ')
    fs.create_file(FOLDERADDRESS + r'/emptyfile03.m')
    fs.create_file(FOLDERADDRESS + r'/folder10/__init__.py')
    fs.create_file(FOLDERADDRESS + r'/folder10/.emptyfile11.C')
    fs.create_file(FOLDERADDRESS + r'/folder10/.emptyfile12.Java')
    fs.create_file(FOLDERADDRESS + r'/.folder11/emptyfile10.txt')
    fs.create_file(FOLDERADDRESS + r'/.folder11/empty file written to 12')
    fs.create_file(FOLDERADDRESS + r'/.folder11/filewithnewline13')
    with open(FOLDERADDRESS + r'/.folder11/filewithnewline13', 'w') as file:
        file.write('\n')
