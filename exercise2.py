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
    The application of input string allows the user to find the location of the substring in the input_string.
    The function would use a for loop to do letter by letter comparison that behaves exactly like a string function.
    :param:The input_string and the substring are strings. The user wants to find the substring within input_string.
    :return:The user will get the location of the substring in the form of an integer.
    """

    # Assign string equals to the input_string with slicing starting from the beginning to the end.
    string = input_string[start:]
    index = 0

    # Enter the for loop to compare the letter of the in the string one by one.
    for character in string:
        if character == substring[0]:
            # The slice of the string is equal to the substring.
            if string[index: index+len(substring)] == substring:
                return index
        index += 1
    # If substring not found within string, return the integer "-1".
    else:
        return -1

def multi_find(input_string, substring, start, end):
    """
    The multi find function allows the user to find all the locations where the substring is found.
    :param:The input_string, substring, and the range of the function in the input_string eg("aaadgda", "dgd", 0, 6) :
    :return:It shall return the indexes of the substring in the input string, eg( 3):
    """
    # Set a empty return string to save variables.
    return_str = ""
    # Set a empty input_index to store number.
    input_index = 0

    index = find(input_string, substring, start, end)
    # If no substring is found in string, return -1
    if index == -1:
                return -1
    else:
        return_str += (',' + str(index))
        # set a new_string equal to the rest of the string after the first matching of substring
        new_string = input_string[index+len(substring)-1:]
        # while loop condition the remaining string is longer than the substring, if the rest of the string is less than substring, so it's impossible to find matching again
        while len(new_string) > len(substring):
            # let index call the function we defined in part a, but switch input_string with new_string
            index = find(new_string, substring, start, end)
            if index == -1:
                # we should return the empty string slicing with 1, after ","
                return return_str[1:]
            # Another else condition inside the loop
            else:
    # add back the length of the substring back to the index, so we don't count starting from the end of the substring
                input_index += index + len(substring)
                # add back the length of the substring again after previous matching
                new_string = new_string[index+len(substring):]
                return_str += ',' + str(input_index)
        # end the loop with the return when the rest of the string is less than substring
        return return_str[1:]

print(multi_find("ccaccacca", "cc", 0, 9))

