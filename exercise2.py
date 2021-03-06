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
    The application of input string, allowing the user to find the location of the substring in the input_string.
    The function would use a for loop to do letter by letter comparison that behave exactly like a string function.
    :param:"input_string" (string), "substring" (string, "start" (integer), "end" (integer)
    :return:The user will get the location of the substring in integer indices.
    """

    # Define the string equal to the input_string with slicing from start to the end.
    string = input_string[start:]
    index = 0
    # Enter the for loop to compare the letter of the in the string one by one.
    for character in string:
        if character == substring[0]:
            # The slice of the string is equivalent to the substring.
            if string[index: index+len(substring)] == substring:
                return index
        index += 1
    else:
        return -1


def multi_find(input_string, substring, start, end):
    """
    Instead of returning one integer index, returns a string with zero or more indices separated by commas
    :The input_string, substring, and the range of the function in the input_string eg("aaadgda", "dgd", 0, 6) :
    :It shall return the indexes of the substring in the input string, eg( 3):
    """
    # Set a empty return string to save variables.
    return_str = ""
    # Set a empty input_index to save number.
    input_index = 0
    substr_length = len(substring)

    # Store the return value by using find function, wait for user's input.
    index = find(input_string, substring, start, end)
    input_index = input_index + index
    if index == -1:
        return return_str
    # If the index doesn't equal to -1, that means there is something found, so enter else condition.
    else:
        return_str += (str(index))
    # Create a for loop to compare the seek multiple substring in the input_string.
    for element in range (start, end-substr_length+2):
        if input_string[element: element+substr_length]==substring:
            return_str += "," + str(element)
    # The return_str will start after ",", so slicing start from 1.
    if return_str != "":
        return_str = return_str[1:]
    return return_str[1:]
