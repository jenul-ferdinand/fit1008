__author__ = 'Maria Garcia de la Banda modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

import unittest
from circular_queue import *

class TestQueue(unittest.TestCase):
    """ Tests for the above class."""
    EMPTY = 0
    ROOMY = 5
    LARGE = 10
    CAPACITY = 20

    def setUp(self):
        self.lengths = [self.EMPTY, self.ROOMY, self.LARGE, self.ROOMY, self.LARGE]
        self.queues = [CircularQueue(self.CAPACITY) for i in range(len(self.lengths))]
        for queue, length in zip(self.queues, self.lengths):
            for i in range(length):
                queue.append(i)
        self.empty_queue = self.queues[0]
        self.roomy_queue = self.queues[1]
        self.large_queue = self.queues[2]
        #we build empty queues from clear.
        #this is an indirect way of testing if clear works!
        #(perhaps not the best)
        self.clear_queue = self.queues[3]
        self.clear_queue.clear()
        self.lengths[3] = 0
        self.queues[4].clear()
        self.lengths[4] = 0

    def tearDown(self):
        for s in self.queues:
            s.clear()

    def test_init(self):
        self.assertTrue(self.empty_queue.is_empty())
        self.assertEqual(len(self.empty_queue), 0)

    def test_len(self):
        """ Tests the length of all queues created during setup."""
        for queue, length in zip(self.queues, self.lengths):
            self.assertEqual(len(queue), length)

    def test_is_empty_add(self):
        """ Tests queues that have been created empty/non-empty."""
        self.assertTrue(self.empty_queue.is_empty())
        self.assertFalse(self.roomy_queue.is_empty())
        self.assertFalse(self.large_queue.is_empty())

    def test_is_empty_clear(self):
        """ Tests queues that have been cleared."""
        for queue in self.queues:
            queue.clear()
            self.assertTrue(queue.is_empty())

    def test_is_empty_serve(self):
        """ Tests queues that have been served completely."""
        for queue in self.queues:
            #we empty the queue
            try:
                while True:
                    was_empty = queue.is_empty()
                    queue.serve()
                    #if we have served without raising an assertion,
                    #then the queue was not empty.
                    self.assertFalse(was_empty)
            except:
                self.assertTrue(queue.is_empty())

    def test_is_full_add(self):
        """ Tests queues that have been created not full."""
        self.assertFalse(self.empty_queue.is_full())
        self.assertFalse(self.roomy_queue.is_full())
        self.assertFalse(self.large_queue.is_full())

    def test_append_and_serve(self):
        for queue in self.queues:
            nitems = self.ROOMY
            for i in range(nitems):
                queue.append(i)
            for i in range(nitems):
                self.assertEqual(queue.serve(), i)

    def test_clear(self):
        for queue in self.queues:
            queue.clear()
            self.assertEqual(len(queue), 0)
            self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    testtorun = TestQueue()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite) 