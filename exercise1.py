#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# identify the five vowel
vowel = "aeiou"
def pig_latinify():
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    # ask user for input of a English word
    word = raw_input("Please enter a English word")
    # if the first letter is vowel, it should return the user word append "yay"
    if word[0] in vowel:
        word = word.lower()
        print (word + "yay")
    #the enter of string index
    index = 0
    #use for loop to find the first vowel in the word
    for element in word:
        if element in vowel:
    #if the word contains multiple consonant, put all of them up to the first vowel to the end with append "ay"
            print (word[index:]+word[0:index] + "ay")
#last but not the least,  call the function
pig_latinify()