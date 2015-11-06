#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

#Additinoal table generated for testing purpose
LIST1 = [["Name", "Sex", "ID"], ["Terry", "Male", 0755], ["Jessica", "Female", 8863], ["Frank","Male", 1103]]
LIST2 = [["Name", "Sex", "ID"], ["Terry", "Male", 0755], ["Nana", "Female", 7766], ["Jowell", "Male", 6688]]
# the table with different schema from other tables
LIST3 = [["Gender", "Age", "ID"],["Male", 23, 1234], ["Female", 44, 9976], ["Male", 32, 8765]]
# this is a table identical with LIST1
LIST4 = [["Name", "Sex", "ID"], ["Terry", "Male", 0755], ["Jessica", "Female", 8863], ["Frank","Male", 1103]]
# this is a table with no intersection to LIST2
LIST5 = [["Name", "Sex", "ID"], ["Karen", "Female", 3188], ["Jessica", "Female", 8863], ["Frank","Male", 1103]]
#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

def test_advanced_union():
    # Test the union function by comparing the additional tables generated
    result = [["Name", "Sex", "ID"],
              ["Terry", "Male", 0755],
              ["Jessica", "Female", 8863],
              ["Frank","Male", 1103],
              ["Nana", "Female", 7766],
              ["Jowell", "Male", 6688]]
    assert is_equal(result, union(LIST1, LIST2))

    #A special situation where two table are completely identical
    result = [["Name", "Sex", "ID"],
              ["Terry", "Male", 0755],
              ["Jessica", "Female", 8863],
              ["Frank","Male", 1103]]
    assert is_equal(result, union(LIST1, LIST4))

def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

def test_advanced_intersection():
    # Test the intersection function by comparing the additional tables generated
    result = [["Name", "Sex", "ID"],["Terry", "Male", 0755]]

    assert is_equal(result, intersection(LIST1, LIST2))

    #A special situation where there are no intersection between two tables
    result = [["Name", "Sex", "ID"]]
    assert is_equal(result, intersection(LIST2, LIST5))

def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

def test_advanced_difference():
    # Test the difference function by comparing the additional tables generated
    result = [["Name", "Sex", "ID"],
              ["Jessica", "Female", 8863],
              ["Frank","Male", 1103]]

    assert is_equal(result, difference(LIST1, LIST2))

    #A special situation where two tables are completely identical
    result = [["Name", "Sex", "ID"]]
    assert is_equal(result, difference(LIST1, LIST4))

    #A special situation where there are no intersection between two tables
    result = [["Name", "Sex", "ID"],
              ["Terry", "Male", 0755],
              ["Nana", "Female", 7766],
              ["Jowell", "Male", 6688]]
    assert is_equal(result, difference(LIST2, LIST5))

def test_MismatchedAttributesException():
    #Test if the function union will capture the error when the schemas are not identical
    try:
         union(LIST1, LIST3)
    except MismatchedAttributesException:
        assert True
    #Test if the function intersection will capture the error when the schemas are not identical
    try:
         intersection(LIST1, LIST3)
    except MismatchedAttributesException:
        assert True
    #Test if the function difference will capture the error when the schemas are not identical
    try:
         difference(LIST1, LIST3)
    except MismatchedAttributesException:
        assert True




