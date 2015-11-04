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
    This function will translate an English word into pig latin. If the word begins with a vowel, it will add "yay" to
    the end of word while words beginning with consonants will append to the end and "ay" will be ended to the end.

    :param : The inputs into this function are strings of English words
    :return: The expected output of this function will return a string translated into pig latin.
    :raises: There are no errors being raised in this exercise.

    """

    # Identify a local variable for vowels.
    vowels = "aeiou"

    # Assigns the appropriate suffix value appropriate to a vowel or consonant
    vowel_pig = "yay"
    consonant_pig = "ay"

    # Variable that assigns a string value
    pig_word = ""

    # Variable that assigns the beginning of an indexing count
    index = 0
    first_vowel = -1

    # Part 1: Find the beginning consonant cluster
    # Check each letter until it reaches a vowel
    for letter in word:
        if letter in vowels:
            first_vowel = index
            break
        index += 1

    # Part 2: Make the new word
    # If no vowel is found, then the function attaches "ay" to the end of the word
    if first_vowel == -1:
        pig_word = word + consonant_pig
    # If the first letter is a vowel, then the function attaches "yay" to the end of the word.
    elif first_vowel == 0:
        pig_word = word + vowel_pig
    # The function gathers words beginning with consonants, appends them to the end, and adds "ay".
    else:
        pig_word = word[first_vowel:] + word[0:first_vowel] + consonant_pig

    # Print word translated into pig latin
    print pig_word

    return pig_word

# pig_latinify("word")