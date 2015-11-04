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
    for item in pig_latinify("dog"):
        assert pig_latinify("dog") == "ogday"

def test_three_consonants():

    for item in pig_latinify("scratch"):
        assert pig_latinify("scratch") == "atchscray"

def test_vowel_first():

    for item in pig_latinify("is"):
        assert pig_latinify("is") == "isyay"

def test_other_word():
    for item in pig_latinify("apple"):
        assert pig_latinify("apple") == "appleyay"

# additional test cases with different varieties
def test_double_dog():
    for item in pig_latinify("ddog"):
        assert pig_latinify("ddog") == "ogdday"

def test_enterprise():
    for item in pig_latinify("enterprise"):
        assert pig_latinify("enterprise") == "enterpriseyay"

def test_three_consonants_again():
    for item in pig_latinify("school"):
        assert pig_latinify("school") == "oolschay"

def test_calculator():
    for item in pig_latinify("calculator"):
        assert pig_latinify("calculator") == "alculatorcay"

def test_clock():
    for item in pig_latinify("clock"):
        assert pig_latinify("clock") == "ockclay"

