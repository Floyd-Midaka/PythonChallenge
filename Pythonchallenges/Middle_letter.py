'''Write  a function named mid that takes a string as its paramater'''
'''your function should extract and return the middle letter'''
'''if there is no middle letter, your function shoud return the empty string'''

from operator import length_hint


def mid(my_string):
    length = len(my_string) % 2
    if length == 0:
        return ""
    elif length != 0:
        middle = len(my_string) // 2
        return my_string[middle]
print (mid("HeeeEllo"))