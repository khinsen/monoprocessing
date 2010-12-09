#!/usr/bin/env python

#
# Unit tests for the monoprocessing package
#
# This is essentially the Pool test case from the multiprocessing
# test suite, minus the timing-specific tests.
#

import unittest
import monoprocessing
import time

def sqr(x, wait=0.0):
    time.sleep(wait)
    return x*x

class TestPool(unittest.TestCase):

    def setUp(self):
        self.pool = monoprocessing.Pool()
    
    def test_apply(self):
        papply = self.pool.apply
        self.assertEqual(papply(sqr, (5,)), sqr(5))
        self.assertEqual(papply(sqr, (), {'x':3}), sqr(x=3))

    def test_map(self):
        pmap = self.pool.map
        self.assertEqual(pmap(sqr, range(10)), map(sqr, range(10)))
        self.assertEqual(pmap(sqr, range(100), chunksize=20),
                         map(sqr, range(100)))

    def test_async(self):
        res = self.pool.apply_async(sqr, (7,))
        self.assertEqual(res.get(), 49)

    def test_imap(self):
        it = self.pool.imap(sqr, range(10))
        self.assertEqual(list(it), map(sqr, range(10)))

        it = self.pool.imap(sqr, range(10))
        for i in range(10):
            self.assertEqual(it.next(), i*i)
        self.assertRaises(StopIteration, it.next)

        it = self.pool.imap(sqr, range(1000), chunksize=100)
        for i in range(1000):
            self.assertEqual(it.next(), i*i)
        self.assertRaises(StopIteration, it.next)

    def test_imap_unordered(self):
        it = self.pool.imap_unordered(sqr, range(1000))
        self.assertEqual(sorted(it), map(sqr, range(1000)))

        it = self.pool.imap_unordered(sqr, range(1000), chunksize=53)
        self.assertEqual(sorted(it), map(sqr, range(1000)))


if __name__ == '__main__':
    unittest.main()
