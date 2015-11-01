#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# User enters a English word to be translated into Pig Latin.
word = raw_input("Enter an English word and press ENTER: ")

def pig_latinify(word):

    # Identify a local variable for vowels.
    vowels = ["a", "e", "i", "o", "u"]

    # Identify a local variable for vowels.
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
              "m", "n", "p", "q", "r", "s", "t", "v", "w",
              "x", "z"]

    # Assigns the appropriate suffix depending if it is a vowel or consonant
    vowel_pig = "yay"
    consonant_pig = "ay"


    # If input word has vowel, it will add "yay" to the end
    if word[0] in vowels:
        print word + vowel_pig

    # If input word begins with 1 consonant, it will add it to the end with "ay"
    elif word[0] in consonants:
        print word[1:] + word[0] + consonant_pig

    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    """
    result = ""

    return result
    """
pig_latinify(word)