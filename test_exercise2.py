#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14


def test_advanced_find_basic():
    """
    Test the find function that will do the same as the find.string method with for loop
    """
    assert find("characteristic","ara", 0, 14) == 2

    # A special situation where the end index is negative number
    assert find("dominating","min", 0, -1) == 2

    # A special situation where substring is identical as input_string

    assert find("homework","homework", 0, 8) == 0


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 15) == "0,4,8,12"


def test_advanced_multi_find_basic():
    """
    Test the if the function will find multiple location of the substring in the index
    """
    assert multi_find("ccaccacca", "c", 0, 9) == '0,1,3,4,6,7'

    # Test when the ending slice is out of range

    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 35) == "0,4,8,12"

    # Test when the substring is identical as input_string

    assert multi_find("assignment", "assignment", 0, 9) == '0'


def test_multi_find_invalid_substring():
    """
    Test if the substring is not in the input_string
    :return: The function should return the user a empty string
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ha", 0, 15) == ""


def test_number_string():
    """
    Test if it will find strings that are numbers in a sentence.
    """
    assert multi_find("Address: 22 Street, Apt. 412, Area Code(212)","2", 0, 44) == "9,10,27,40,42"
