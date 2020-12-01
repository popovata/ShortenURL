""" rwlock.py
    A class to implement read-write locks on top of the standard threading
    library.
"""

from contextlib import contextmanager
from threading import Lock


class RWLock(object):
    """ Read-write Lock class; this is meant to allow an object to be read from by
        multiple threads, but only written to by a single thread at a time
    """

    def __init__(self):
        """
        Create an instance of the class
        """
        self.w_lock = Lock()
        self.num_r_lock = Lock()
        self.num_r = 0

    # ___________________________________________________________________
    # Reading methods

    def r_acquire(self):
        """
        Locks the read lock
        """
        self.num_r_lock.acquire()
        self.num_r += 1
        if self.num_r == 1:
            self.w_lock.acquire()
        self.num_r_lock.release()

    def r_release(self):
        """
        Release read lock
        """
        assert self.num_r > 0
        self.num_r_lock.acquire()
        self.num_r -= 1
        if self.num_r == 0:
            self.w_lock.release()
        self.num_r_lock.release()

    @contextmanager
    def r_locked(self):
        """
        This method is designed to be used via the `with` statement
        """
        try:
            self.r_acquire()
            yield
        finally:
            self.r_release()

    # ___________________________________________________________________
    # Writing methods.

    def w_acquire(self):
        """
        Locks the write lock
        """
        self.w_lock.acquire()

    def w_release(self):
        """
        Releases the read lock
        :return:
        """
        self.w_lock.release()

    @contextmanager
    def w_locked(self):
        """
        This method is designed to be used via the `with` statement
        """
        try:
            self.w_acquire()
            yield
        finally:
            self.w_release()
