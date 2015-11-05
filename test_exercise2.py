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

def test_find_basic():
    """
    Test the find function that will do excatly the same as the find.string method with for loop
    """
    assert find("characteristic","ara", 0, 14) == 2

def test_multi_find_basic():
    """
    Test the multi find function
    """
    assert find("ccaccacca","c",0,8) == "0,1,3,4,6,7"


def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"
