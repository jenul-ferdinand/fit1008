from queue_adt import Queue
from typing import TypeVar
from referential_array import ArrayR

T = TypeVar('T')

class CircularQueue(Queue):
    MIN_CAPACITY = 1
    
    def __init__(self, max_capacity) -> None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def append(self,item:T) -> None:
        """ Adds an element to the rear of the queue."""
        if self.is_full():
            raise Exception("Queue is full")
        
        self.array[self.rear] = item
        self.length += 1
        self.rear = (self.rear + 1) % len(self.array)

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front."""
        if self.is_empty():
            raise Exception("Queue is empty")
        
        self.length -= 1
        item = self.array[self.front]
        self.front = (self.front+1) % len(self.array)
        return item

    def __len__(self) -> int:
        """ Returns the number of elements in the queue."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the queue is empty. """
        return len(self) == 0

    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        return len(self) == len(self.array)

    def clear(self):
        """ Clears all elements from the queue. """
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
