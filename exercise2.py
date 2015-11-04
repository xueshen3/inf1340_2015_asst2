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
    :raises:resulting a error when the input in the form other than string

    """
    string = input_string[start:end+1]
    index = 0
    for character in string:
        if character == substring[0]:
            if string[index: index+len(substring)] == substring:
                return index
        index += 1
    else:
        return -1

print(find("assignment","ssign",0,9))

def multi_find(input_string, substring, start, end):
    """
    The application of multi string function, the function allow users to find all the location where substring is found
    :The input_string, substring, and the range of the function in the input_string eg("aaadgda", "dgd", 0, 6) :
    :It shall return the indexes of the substring in the input string, eg( 3):
    :raises:

    """
    #set a empty return string to save variables
    return_str = ""
    #set a empty input_index to store number
    input_index = 0

    # store the return value by find function, wait for user's input
    index = find(input_string, substring, start, end)
    # apply the function of the first function, if no substring is found in string
    if index == -1:
    # if cannot find anything, return a empty string
        return return_str
    # if the index doesn't equal to -1, that means there is something found, so enter else condition
    else:
        # found the first match and save the match to return_str
        return_str += (', ' + str(index))
        # set a new_string equal to the rest of the string after the first matching of substring
        new_string = input_string[index+len(substring):]
        # set a while loop if the rest of the string is greater than the substring, if the rest of the string is less than substring, so it's impossible to find matching again
        while len(new_string) > len(substring):
        # let index call the function we defined in part a, but switch input_string with new_string
            index = find(new_string, substring, start, end)
        # if we cannot find anything, we return immediately
            if index == -1:
        # we should return the empty string slicing with 2, after ", "
                return return_str[2:]
        # Another else condition inside the loop
            else:
        # add back the length of the substring back to the index, so we don't count starting from the end of the substring
                input_index += index + len(substring)
        # add back the length of the substring again after previous matching
                new_string = new_string[index+len(substring):]
        # return the number of the location
                return_str += ', ' + str(input_index)
        # end the loop with the return when the rest of the string is less than substring
        return return_str[2:]

print(multi_find('substringtriabctriabc','tri',0,20))

