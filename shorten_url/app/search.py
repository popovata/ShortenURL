from app.utils import get_random_alphanumeric_string


class ShortKeys:
    """ A class used to represent a dictionary
        where values are given by users and keys are generated in this class

    ...

    Attributes
    ----------
    key_to_url : dict
        a dictionary that store values are given by users and generated keys

    Methods
    -------
    add_key(value)
        adds new pair key-value to dictionary

    __find_unique_key()
        generates random strings until find a key that are not in dictionary


    """

    def __init__(self, key_length):
        """ Create an empty dictionary."""
        self.key_to_url = {}
        self.key_length = key_length

    def add_key(self, url):
        """ Adds new pair key-value to dictionary

        :param url: string that was given by user
        :return: generated key for given value
        """
        short_key = self.__find_unique_key()
        self.key_to_url[short_key] = url
        return short_key

    def __find_unique_key(self):
        """ Looks for a key that are not in dictionary yet

        :return: found key
        """
        key = get_random_alphanumeric_string(self.key_length)
        while key in self.key_to_url:  # do..while  использовать константу, передавать длину ключа как параметр
            key = get_random_alphanumeric_string(self.key_length)
        return key

    def get_url(self, key):
        """Returns a value by a given key"""
        return self.key_to_url.get(key)
