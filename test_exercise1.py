#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin
Test module for exercise1.py
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

    # Test case for multiple consonants
    assert pig_latinify("synchronize") == "onizesynchray"
    assert pig_latinify("dday") == "aydday"

    # Test case for no vowels
    assert pig_latinify("why") == "whyay"

    # Test case for multiple vowels
    assert pig_latinify("aaa") == "aaayay"
