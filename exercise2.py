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
    :Param:The input_string and the substring where users want to find in the input_string, along with the range in input_string :
    :return:The user will get the location of the substring in the form of index.
    :raises:

    """
    string = input_string[start:end+1]
    index = 0
    for character in string:
        if character == substring[0]:
            if string[index: index+len(substring)] == substring:
                return string.find(substring)
        index += 1
    else:
        return -1
print(find("assignment","ssign",0,9))

def multi_find(input_string, substring, start, end):
    """
    The application of multi string function, the function allow users to find all the location where substring is found
    :The input_string, substring, and the range of the function in the input_string eg("aaadgdaaadgd", "dgd", 0, 11) :
    :It shall return the indexes of the substring in the input string, eg( 3, 9):
    :raises:

    """
    return_str = " "
    input_index = 0

    # store the return value by find function
    index = find(input_string, substring, start, end)
    if index == -1:
        return return_str
    else:
        return_str += (', ' + str(index))
        new_string = input_string[index+len(substring):]
        while len(new_string) > len(substring):
            index = find(new_string, substring, start, end)
            if index == -1:
                return return_str[2:]
            else:
                input_index = input_index + index
                new_string = new_string[index+len(substring):]
                input_index += len(substring)
                return_str += ', ' + str(input_index)
        return return_str[2:]

print(multi_find('substringtriabctriabc','tri',0,20))

