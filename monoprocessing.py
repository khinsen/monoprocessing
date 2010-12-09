# A dummy version of the class multiprocessing.Pool for debugging.
# All tasks submitted to the pool are executed immediately in the
# same process.
#
# Written by Konrad Hinsen

import itertools

class Pool(object):
    '''
    A dummy version of the class multiprocessing.Pool for use in
    debugging.

    All tasks submitted to the pool are executed immediately in the
    same process.
    '''
    
    def __init__(self, processes=None, initializer=None, initargs=()):
        pass

    def apply(self, func, args=(), kwds={}):
        '''
        Equivalent of `apply()` builtin
        '''
        return apply(func, args, kwds)

    def apply_async(self, func, args=(), kwds={}, callback=None):
        '''
        Pseudo-asynchronous equivalent of `apply()` builtin
        '''
        result = AsyncResult(apply(func, args, kwds))
        if callback is not None:
            callback(result.get())
        return result

    def map(self, func, iterable, chunksize=None):
        '''
        Equivalent of `map()` builtin
        '''
        return map(func, iterable)

    def map_async(self, func, iterable, chunksize=None, callback=None):
        '''
        Pseudo-asynchronous equivalent of `map()` builtin
        '''
        if not hasattr(iterable, '__len__'):
            iterable = list(iterable)
        result = AsyncResult(map(func, iterable))
        if callback is not None:
            callback(result.get())
        return result

    def imap(self, func, iterable, chunksize=1):
        '''
        Equivalent of `itertools.imap()``
        '''
        return itertools.imap(func, iterable)

    imap_unordered = imap

    def close(self):
        pass

    def terminate(self):
        pass

    def join(self):
        pass


class AsyncResult(object):

    def __init__(self, value):
        self.value = value

    def get(self, timeout=None):
        return self.value

    def wait(self, timeout=None):
        pass

    def ready(self):
        return True

    def successful(self):
        return True
