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

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 15) == "0,4,8,12"

def test_advanced_find_basic():
    """
    Test the find function with more extraordinary situation
    """
    assert find("characteristic","ara", 0, 14) == 2

    # A special situation where the end index is negative number
    assert find("dominating","min", 0, -1) == 2

    # A special situation where substring is identical as input_string

    assert find("homework","homework", 0, 8) == 0

    # Test when only ranging the portion of the input_string

    assert find("honeyhoneyhoney","ney", 0, 5) == 2

    # Test when the end index is out of range

    assert find("honey","ney", 0, 15) == 2

def test_advanced_multi_find_basic():
    """
    Test the multi find function with many different situation
    """

    assert multi_find("ccaccacca", "c", 0, 9) == "0,1,3,4,6,7"

    # Test when the ending slice is out of range

    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 35) == "0,4,8,12"

    # Test when the substring is identical as input_string

    assert multi_find("book", "book", 0, 3) == "0"

    #Test when only ranging the first portion of the input_string

    assert multi_find("winterwinterwinter", "ter", 0, 5) == "3"

    #Test when only ranging from the last portion of the input_string

    assert multi_find("winterwinterwinter", "ter", 12, 17) == "15"

def test_find_invalid_substring():

    #Test if the substring is not in the input_string

    assert find("homogeneous","bob", 0, 12) == -1

    assert find("identification","low", 0, 22) == -1

    assert find("service_department","man", 0, 12) == -1

    assert find("fire_work","ide", 0, 10) == -1


def test_multi_find_invalid_substring():

    #Test if the substring is not in the input_string.

    assert multi_find("Ni! Ni! Ni! Ni!", "Ha", 0, 15) == ""

    assert multi_find("Halloween", "kee", 0, 9) == ""

    assert multi_find("Toronto_Pearson_Airport", "go", 0, 31) == ""

    assert multi_find("loading_message","lol", 0, 15) == ""

def test_num_string():
    
    # Test if the substring will return a string integer.

    assert multi_find("Address: 22 Street, Apt. 412, Area Code(212)", "2", 0, 44) == "9,10,27,40,42"