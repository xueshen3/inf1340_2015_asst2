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


def test_consonants_y():
    # Test case with multiple consonants and y as a consonant
    assert pig_latinify("synchronize") == "onizesynchray"
    assert pig_latinify("psychology") == "ologypsychay"

def test_consonants():
    # Test case starting with consonants
    assert pig_latinify("dday") == "aydday"
    assert pig_latinify("ssnakes") == "akesssnay"

def test_no_consonants():
    # Test case for no vowels
    assert pig_latinify("why") == "whyay"
    assert pig_latinify("try") == "tryay"
    assert pig_latinify("hmmm") == "hmmmay"

def test_all_vowels():
    # Test case for only vowels
    assert pig_latinify("aaa") == "aaayay"
    assert pig_latinify("eeee") == "eeeeyay"
