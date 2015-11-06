#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def union(table1, table2):
    """
    The function would perform the union set operation on user's tables, named table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the new table generated after union table operation,
             returns a new table that contains all unique rows that appear in either table
    :raises: when the schemas of two tables are not the same, raise MismatchedAttributesException:
    """

    # create a new_list to display the value in the new table generated
    new_list = []
     # check if the table columns and the schema are equal
    if table1[0] == table2[0]:
     # created a for loop to compare the value in table 1 and 2
        for element in table1:
            new_list.append(element)
        for element in table2:
            # if the value in table2 is not in table1, we add it input the new_list
            if element not in new_list:
                new_list.append(element)
        return new_list
    # raise the MismatchedAttributes Exception error if schemas don't match
    else:
        raise MismatchedAttributesException

    return []


def intersection(table1, table2):
    """
    The function will perform a intersection set row of the two tables
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the new table generated after intersection table operation,
             returns a new table that contains all unique rows that appear in both tables.
    :raises: when the schemas of two tables are not the same, raise MismatchedAttributesException:

    """
    new_list = []
    # check if the table columns and the schema are equal
    if table1[0] == table2[0]:
    # created a for loop to compare the value in table1 and table2
        for element in table1:
            # if the value is table1 is also in table2, we put it input the new_list
            if element in table2:
                new_list.append(element)
        return new_list
    # raise the MismatchedAttributes Exception error if schemas don't match
    else:
        raise MismatchedAttributesException
    return []

def difference(table1, table2):
    """
    The function will perform a difference set row of the two tables
    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the new table generated after difference table operation,
             returns a new table that contains all unique rows that appear in the first table but not the second.
    :raises: when the schemas of two tables are not the same, raise MismatchedAttributesException:
    """
    new_list = []
    # check if the table columns and the schema are equal
    if table1[0] == table2[0]:
        new_list.append(table1[0])
        # created a for loop to compare the value in table1 and table2
        for element in table1:
            #if the value in table 1 is not in table2, we put it into the new_list
            if element not in table2:
                new_list.append(element)
        return new_list
    # raise the MismatchedAttributes Exception error if schemas don't match
    else:
            raise MismatchedAttributesException
    return []

########################
### HELPER FUNCTIONS ###
########################
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

