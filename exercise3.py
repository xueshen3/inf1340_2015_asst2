#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

GRADUATES = [["Number", "Surname", "Age"], [7274, "Robinson", 37], [7432, "O'Malley", 39],[9824, "Darkes", 38]]
GRADUATES1 = [["Number", "Surname", "Age"],[7474, "Robinson", 37],[7432, "O'Malley", 39],[9824, "Darkes", 38]]

def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    new_list = []
     # check table columns and schema are equal
    if table1[0] == table2[0]:
        for element in table1:
            new_list.append(element)
        for element in table2:
            if element not in new_list:
                new_list.append(element)
        return new_list
    else:
        raise MismatchedAttributesException


    return []


def intersection(table1, table2):
    """
    Describe your function

    """
    new_list = []
    if table1[0] == table2[0]:
        for element in table1:
            if element in table2:
                new_list.append(element)
        return new_list
    else:
        raise MismatchedAttributesException
    return []


def difference(table1, table2):
    """
    Describe your function

    """
    new_list = []
    if table1[0] == table2[0]:
        for element in table1:
            if element not in table2:
                new_list.append(element)
        for element in table2:
            if element not in table1:
                new_list.append(element)
        return new_list
    else:
            raise MismatchedAttributesException 
    return []


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

