"""
Unit test for the class File from the module efd.file

"""

__author__ = "Behzad"

import pytest

from efd.file import File
from tests.conftest import FOLDERADDRESS

KnownFilesTestCases = [(FOLDERADDRESS + r'/emptyfile01.INI', ';'),
                       (FOLDERADDRESS + r'/emptyfile03.m', '%'),
                       (FOLDERADDRESS + r'/folder10/__init__.py', '#'),
                       (FOLDERADDRESS + r'/folder10/.emptyfile11.C', '//'),
                       (FOLDERADDRESS + r'/folder10/.emptyfile12.Java', '//')]


def test_file_has_address(fake_file_system):
    """Test if the File object has address"""
    fileAddress = FOLDERADDRESS + r'/file00.txt'
    testfile = File(fileAddress)
    assert fileAddress == testfile.address


def test_if_empty_file_is_detected(fake_file_system):
    fileAddress = FOLDERADDRESS + r'/emptyfile01.ini'
    testfile = File(fileAddress)
    assert testfile.isempty()


def test_if_file_with_space_character_is_not_considered_empty(
        fake_file_system):
    fileAddress = FOLDERADDRESS + r'/filecontainingspace02.m'
    testfile = File(fileAddress)
    assert not testfile.isempty()


def test_if_file_with_newline_character_is_not_considered_empty(
        fake_file_system):
    fileAddress = FOLDERADDRESS + r'/.folder11/filewithnewline13'
    testfile = File(fileAddress)
    assert not testfile.isempty()


def test_filling_an_emtpyfile(fake_file_system):
    fileAddress = FOLDERADDRESS + r'/.folder11/empty file written to 12'
    testfile = File(fileAddress)
    wasItEmpty = testfile.isempty()
    testfile.fill('dummy text')
    with open(fileAddress, 'r') as file:
        retrievedText = file.read()
    assert (not testfile.isempty()) and wasItEmpty \
        and retrievedText == 'dummy text'


def test_warning_if_fillmethod_runs_on_non_empty_file(fake_file_system):
    fileAddress = FOLDERADDRESS + r'/filecontainingspace02.m'
    testfile = File(fileAddress)
    with pytest.warns(UserWarning):
        testfile.fill()


@pytest.mark.parametrize("fileAddress, expectedFiller", KnownFilesTestCases)
def test_autofilling_for_known_files(fake_file_system, fileAddress,
                                     expectedFiller):
    """Test correct filler is used in absence of filler given by user

    For known files if the user does not determine what to be written
    in the file, the program should fill the file with commenting mark
    appropriate for the file type."""
    testfile = File(fileAddress)
    testfile.fill()
    with open(testfile.address, 'r') as file:
        assert expectedFiller == file.read()


def test_overriding_autofilling_for_known_files(fake_file_system):
    """Test custom string overrides the default filler

    For the known files such as .ini, there is a default filler, ';'.
    However, if the user determines what to be written in the file, the
    user input should be used rather than the default value."""
    fileAddress = FOLDERADDRESS + r'/emptyfile01.INI'
    testfile = File(fileAddress)
    text = 'arbitrarytext'
    testfile.fill(text) # a string is passed to the method
    with open(testfile.address, 'r') as file:
        assert text == file.read()
