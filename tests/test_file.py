"""
Unit test for the class File from the module efd.file

"""

__author__ = "Behzad"

import hashlib

import pytest

from efd.file import File
from tests.conftest import FOLDERADDRESS

KNOWNFILESTEXTCASES = [(FOLDERADDRESS + r'/emptyfile01.INI', ';'),
                       (FOLDERADDRESS + r'/emptyfile03.m', '%'),
                       (FOLDERADDRESS + r'/folder10/__init__.py', '#'),
                       (FOLDERADDRESS + r'/folder10/.emptyfile11.C', '//'),
                       (FOLDERADDRESS + r'/folder10/.emptyfile12.Java', '//')]


def md5(filename):
    """Calculate MD5 checksum of the file"""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def test_file_has_address(fake_file_system):
    """Test if the File object has address"""
    # pylint: disable= unused-argument
    file_address = FOLDERADDRESS + r'/file00.txt'
    testfile = File(file_address)
    assert file_address == testfile.address


def test_if_empty_file_is_detected(fake_file_system):
    # pylint: disable= unused-argument, missing-function-docstring
    file_address = FOLDERADDRESS + r'/emptyfile01.ini'
    testfile = File(file_address)
    assert testfile.isempty()


def test_if_file_with_space_character_is_not_considered_empty(
        fake_file_system):  # pylint: disable= unused-argument
    # pylint: disable= missing-function-docstring
    file_address = FOLDERADDRESS + r'/filecontainingspace02.m'
    testfile = File(file_address)
    assert not testfile.isempty()


def test_if_file_with_newline_character_is_not_considered_empty(
        fake_file_system):  # pylint: disable= unused-argument
    # pylint: disable= missing-function-docstring
    file_address = FOLDERADDRESS + r'/.folder11/filewithnewline13'
    testfile = File(file_address)
    assert not testfile.isempty()


def test_filling_an_emtpyfile(fake_file_system):
    """Test that an empty file is successfully filled with a string"""
    # pylint: disable= unused-argument
    file_address = FOLDERADDRESS + r'/.folder11/empty file written to 12'
    testfile = File(file_address)
    was_it_empty = testfile.isempty()
    testfile.fill('dummy text')
    with open(file_address, 'r') as file:
        retrieved_text = file.read()
    assert (not testfile.isempty()) and was_it_empty \
        and retrieved_text == 'dummy text'


def test_warning_if_fillmethod_runs_on_non_empty_file(fake_file_system):
    """Test that non-empty file being filled is prevented.

    If the file is not empty and the :meth: `emf.File.fill` is called, a
    warning should be raised and nothing happens to the file (the hash key
    remains the same)."""
    # pylint: disable= unused-argument
    file_address = FOLDERADDRESS + r'/filecontainingspace02.m'
    filehash_before = md5(file_address)
    testfile = File(file_address)
    with pytest.warns(UserWarning):
        testfile.fill()
    assert filehash_before == md5(file_address)


@pytest.mark.parametrize("file_address, expected_filler", KNOWNFILESTEXTCASES)
def test_autofilling_for_known_files(fake_file_system, file_address,
                                     expected_filler):
    """Test correct filler is used in absence of filler given by user

    For known files if the user does not determine what to be written
    in the file, the program should fill the file with commenting mark
    appropriate for the file type."""
    # pylint: disable= unused-argument
    testfile = File(file_address)
    testfile.fill()
    with open(testfile.address, 'r') as file:
        assert expected_filler == file.read()


def test_overriding_autofilling_for_known_files(fake_file_system):
    """Test custom string overrides the default filler

    For the known files such as .ini, there is a default filler, ';'.
    However, if the user determines what to be written in the file, the
    user input should be used rather than the default value."""
    # pylint: disable= unused-argument
    file_address = FOLDERADDRESS + r'/emptyfile01.INI'
    testfile = File(file_address)
    text = 'arbitrarytext'
    testfile.fill(text)  # a string is passed to the method
    with open(testfile.address, 'r') as file:
        assert text == file.read()
