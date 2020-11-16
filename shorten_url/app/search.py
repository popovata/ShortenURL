""" A file keeps singleton class KeyToUrl. This class represents a dictionary
    where values are given by users and keys are generated in this class.

"""
from app.utils import get_random_alphanumeric_string
import threading

lock = threading.Lock()

class ShortnerManagerSingleton(type):
    """ Metaclass of class KeyToUrl

    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Function executes every time that object of class KeyToUrl is calling
        
        :return:instance of class
        """
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(ShortnerManagerSingleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]


class KeyToUrl(object):
    """ A class represents a dictionary
        where values are given by users and keys are generated in this class

    ...

    Attributes
    ----------
    key_to_url : dict
        a dictionary that store values are given by users and generated keys

    Methods
    -------
    add_key(value)
        adds generated for URL key and url to the dictionary

    __find_unique_key()
        generates random strings until find a key that are not in dictionary


    """

    __metaclass__ = ShortnerManagerSingleton
    def __init__(self, key_length):
        """ Create an instance of the class"""
        self.key_to_url = {}
        self.key_length = key_length

    def add_key(self, url):
        """ Adds generated for URL key and url to the dictionary

        :param url: string that was given by user by typing to the textbox in the application
        :return: generated key for given value
        """
        short_key = self.__find_unique_key()
        self.key_to_url[short_key] = url
        return short_key

    def __find_unique_key(self):
        """ Looks for a key that are not in dictionary yet

        :return: found key
        """
        key = None
        while key in self.key_to_url:
            key = get_random_alphanumeric_string(self.key_length)
        return key

    def get_url(self, key):
        """ Returns a value by a given key
        :param key: A string is a key to find right url
        :return: right url
        """
        return self.key_to_url.get(key)
