""" Circular Queue ADT with an array implementation. """

__author__ = 'Maria Garcia de la Banda'
__author__ = 'Maria Garcia de la Banda modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from queue_adt import *
from referential_array import ArrayR

class CircularQueue(Queue[T]):
    """ Circular implementation of a queue with arrays.

    Attributes:
         length (int): number of elements in the queue (inherited)
         front (int): index of the element at the front of the queue
         rear (int): index of the first empty space at the oback of the queue
         array (ArrayR[T]): array storing the elements of the queue

    ArrayR cannot create empty arrays. So MIN_CAPACITY used to avoid this.
    """

    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 1) -> None:
        """ Initialisation. """
        self.clear()
        self.array = ArrayR(max(self.MIN_CAPACITY, capacity))

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue.
        :pre: queue is not full
        :raises Exception: if the queue is full
        :complexity: O(1)
        """
        if self.is_full():
            raise Exception("Queue is full")
        
        # Add the value to the rear
        self.array[self.rear] = item
        
        # Increment the length
        self.length += 1 
        
        # Update the rear
        self.rear = (self.rear + 1) % len(self.array)

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front.
        :pre: queue is not empty
        :raises Exception: if the queue is empty
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        
        item = self.array[self.front]
        self.front = (self.front + 1) % len(self.array)
        self.length -= 1
        return item

    def is_full(self) -> bool:
        """ True if the queue is full and no element can be appended. """
        return len(self) == len(self.array)

    def clear(self) -> None:
        """ Clears all elements from the queue. """
        Queue.clear(self)
        self.front, self.rear = 0, 0

    def __str__(self) -> None:
        """ Magic method constructing a string representation of the list object. """

        elems = []
        for i in range(self.length):
            elems.append(str(self.array[(self.front + i) % len(self.array)]))
        return f"[[ {' -> '.join(elems)} ]]"