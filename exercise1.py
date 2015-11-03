#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):

    """
    Describe your function

    :param :
    :return:
    :raises:

    """

    # Identify a local variable for vowels.
    vowels = ["a", "e", "i", "o", "u"]

    # Assigns the appropriate suffix depending if it is a vowel or consonant
    vowel_pig = "yay"
    consonant_pig = "ay"

    pig_word = ""

    index = 0
    first_vowel = -1

    # Part 1: Find the beginning consonant cluster
    # Check each letter until it reaches a vowel
    for letter in word:
        if letter in vowels:
            # figure out how to stop counting once it reaches a vowel
            first_vowel = index
            break
        index += 1

        # Part 2: Make the new word
    if first_vowel == -1:
            # no vowel was found
        pig_word = word + consonant_pig
    elif first_vowel == 0:
        pig_word = word + vowel_pig
    else:
        pig_word = word[first_vowel:] + word[0:first_vowel] + consonant_pig

    print pig_word

    return pig_word

pig_latinify("word")