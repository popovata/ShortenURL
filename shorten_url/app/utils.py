"""
A file is for helpful functions

"""
import random
import string

LETTERS_AND_DIGITS = string.ascii_letters + string.digits


def get_random_alphanumeric_string(length):
    """
    Generates a random string by a given string length

    :param length: length of a result string
    :return: a random string

    """
    return ''.join(random.choice(LETTERS_AND_DIGITS) for i in range(length))
