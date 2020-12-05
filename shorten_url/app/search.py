"""
A file keeps singleton class KeyToUrl. This class represents a dictionary
where values are given by users and keys are generated in this class.
"""
from app.utils import get_random_alphanumeric_string
from threading import Lock
from rwlock import RWLock
from redis import Redis
from app import app

SHORT_KEY_LENGTH = 5
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0


class SingletonMetaclass(type):
    """
    Singleton metaclass
    """
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(SingletonMetaclass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class KeyToUrl(object):
    """
    A thread safe class represents a dictionary
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
        generates random strings until finding a key that is not in the dictionary
    """

    __metaclass__ = SingletonMetaclass

    def __init__(self, key_length=SHORT_KEY_LENGTH):
        """
        Create an instance of the class

        :param key_length: length of dictionary key
        """
        self.key_to_url = Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], db=app.config['REDIS_DB'])
        self.key_length = key_length
        self.read_write_lock = RWLock()

    def add_key(self, url):
        """
        Adds generated for URL key and url to the dictionary

        :param url: string that was given by user by typing to the textbox in the application
        :return: generated key for given value
        """
        with self.read_write_lock.r_locked():
            key = self.__find_unique_key()
        with self.read_write_lock.w_locked():
            self.key_to_url.set(key, url)
        return key

    def __find_unique_key(self):
        """
        Looks for a key that does not exist in the dictionary yet

        :return: found key
        """
        key = None
        while key is None or self.key_to_url.exists(key):
            key = get_random_alphanumeric_string(self.key_length)
        return key

    def get_url(self, key):
        """
        Returns a value by a given key

        :param key: A string represents a key to find right url
        :return: right url
        """
        with self.read_write_lock.r_locked():
            return self.key_to_url.get(key)
