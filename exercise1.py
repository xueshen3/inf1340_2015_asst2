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
    :return: The function will translate the word into a Pig Latin
            If the first letter is vowel, the letter will be append "yay" eg1 (appleyay)
            If the first letter is not a vowel, all consonant up to first vowel will be placed to the end, add "ay"
            eg2 (elcomeway)
    :raises: There are no raises in this function

    """

    # Identify a local variable for vowels.
    vowels = ["a","e", "i", "o", "u"]

    # Assigns the appropriate suffix depending if it is a vowel or consonant
    vowel_pig = "yay"
    consonant_pig = "ay"

    pig_word = ""

    index = 0
    first_vowel = -1
    # Part 1: Find the beginning consonant cluster
    # Use for loop to check each letter until it reaches a vowel
    for letter in word:
        if letter in vowels:
            # figure out how to stop counting once it reaches a vowel, and set the first vowel as index
            first_vowel = index
            break
        else:
            index += 1
        # Part 2: Make the new word
        # when there's no vowel found in the word
        # is_vowel
    if first_vowel == -1:
            # return the word with "ay" at the end of the word
        pig_word = word[:index] + word[index:] + consonant_pig
            # when the first letter is found to be a vowel
    elif first_vowel == 0:
            # return the word with "yay" at the end of the word
        pig_word = word + vowel_pig
            # for other situation, put the consonants up to the first vowel to the end the word, then add "ay"
    else:
         pig_word = word[first_vowel:] + word[0:first_vowel] + consonant_pig

    print pig_word
            # the end of the function
    return pig_word

# last but not the least, call the function
pig_latinify("word")