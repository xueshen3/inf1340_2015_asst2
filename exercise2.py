#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    The function would use a for loop to do letter by letter comparison that behave exactly like a string function

    :param :
    :return:
    :raises:

    """
    string = input_string[start:end+1]
    index = 0
    for character in string:
        if character == substring[0]:
            if string[index: index+len(substring)] == substring:
                return True
        index += 1
    return -1


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result

