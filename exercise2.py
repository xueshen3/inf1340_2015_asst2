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
    return_str = ''
    input_index = 0

    # store the return value by find function
    index = find(input_string, substring,start,end)
    if index == -1:
        return return_str
    else:
        return_str += (', ' + str(index))
        new_string = input_string[index+len(substring):]
        while len(new_string) > len(substring):
            index = find(new_string, substring,start,end)
            if index == -1:
                return return_str[2:]
            else:
                input_index = input_index + index
                new_string = new_string[index+len(substring):]
                input_index += len(substring)
                return_str += ', ' + str(input_index)
        return return_str[2:]

print(multi_find('abadfabasdababfsdfasdfaab','ab',0,30))

