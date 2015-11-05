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
    The function is a tool to translate the any English word of input in to Pig Latin word by applying for loop

    :param : The user will enter any English word (String). eg1 (apple) eg2 (welcome)
    :return: The function will translate the word (String) into a Pig Latin.
            If the first letter is vowel, the letter will be append "yay". eg1 (appleyay)
            If the first letter is not a vowel, all consonant up to first vowel will be placed at the end, add "ay".
            eg2 (elcomeway)
    """

    # Identify a local variable for vowels.
    vowels = ["a","e", "i", "o", "u"]

    # Assign the appropriate suffix depending if it is a vowel or consonant.
    vowel_suffix = "yay"
    consonant_suffix = "ay"

    pig_word = ""

    index = 0
    first_vowel = -1

    # Part 1: Find the beginning consonant cluster
    # Use for loop to check each letter until it reaches a vowel.
    for letter in word:
        if letter in vowels:
            first_vowel = index
            break
        else:
            index += 1

    # Part 2: Make the new word
    # No vowel found so it adds "ay" to the end of the word
    if first_vowel == -1:
        pig_word = word[:index] + word[index:] + consonant_suffix

    # First letter is a vowel, so it adds "yay" to the end of the word
    elif first_vowel == 0:
        pig_word = word + vowel_suffix

    # Take all the consonants up to the first vowels, add them to end, and add "ay"
    else:
         pig_word = word[first_vowel:] + word[0:first_vowel] + consonant_suffix

    return pig_word

# pig_latinify(word)