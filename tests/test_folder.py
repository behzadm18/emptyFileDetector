"""
Unit test for the class Folder from the module efd.folder
fake_file_system is the fixture defined in :mod:`tests:conftest`

"""

__author__ = "Behzad"


import pytest

from efd.folder import Folder
from tests.conftest import FOLDERADDRESS


def test_folder_has_address(fake_file_system):
    """Test if the Folder object has address"""
    # pylint: disable= unused-argument
    testfolder = Folder(FOLDERADDRESS)
    assert FOLDERADDRESS == testfolder.address


def test_folder_does_not_exist(fake_file_system):
    """Test if non-existing folder raises exception"""
    # pylint: disable= unused-argument
    with pytest.raises(FileNotFoundError):
        Folder(r'c:\some\arbitraryAddress')


def test_files_are_found_in_the_folder(fake_file_system):
    """Test all files are found recursively in the folder"""
    # pylint: disable= unused-argument
    testfolder = Folder(FOLDERADDRESS)
    expected_set = {'\\folder_test\\.folder11\\empty file written to 12',
                    '\\folder_test\\.folder11\\filewithnewline13',
                    '\\folder_test\\folder10\\__init__.py',
                    '\\folder_test\\.folder11\\emptyfile10.txt',
                    '\\folder_test\\file00.txt',
                    '\\folder_test\\filecontainingspace02.m',
                    '\\folder_test\\file00.txt',
                    '\\folder_test\\emptyfile01.INI',
                    '\\folder_test\\folder10\\.emptyfile11.C',
                    '\\folder_test\\emptyfile03.m',
                    '\\folder_test\\folder10\\.emptyfile12.Java'}
    file_set = testfolder.all_files()
    assert expected_set == file_set
