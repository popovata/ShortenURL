from app.utils import get_random_alphanumeric_string, SHORT_KEY_LENGTH


class ShortKeys:
    """ A class used to represent a dictionary
        where values are given by users and keys are generated in this class

    ...

    Attributes
    ----------
    urls : dict
        a dictionary that store values are given by users and generated keys

    Methods
    -------
    add_key(value)
        adds new pair key-value to dictionary

    __find_unique_key()
        generates random strings until find a key that are not in dictionary


    """
    def __init__(self):
        """ Create an empty dictionary."""
        self.urls = {}
    def add_key(self, value):
        """ Adds new pair key-value to dictionary

        :param value: string that was given by user
        :return: generated key for given value
        """
        short_key = self.__find_unique_key()
        self.urls[short_key] = value
        return short_key
    def __find_unique_key(self):
        """ Looks for a key that are not in dictionary yet

        :return: found key
        """
        key = get_random_alphanumeric_string(SHORT_KEY_LENGTH)
        while key in self.urls: #do..while  использовать константу, передавать длину ключа как параметр
            key = get_random_alphanumeric_string(SHORT_KEY_LENGTH)
        return key

