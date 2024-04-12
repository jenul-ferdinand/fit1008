""" Queue ADT. """

__author__ = 'Maria Garcia de la Banda modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')

class Queue(ABC, Generic[T]):
    """ Abstract class for a generic Queue. """

    def __init__(self) -> None:
        """ Initialisation. """
        self.length = 0

    @abstractmethod
    def append(self,item:T) -> None:
        """ Adds an element to the rear of the queue."""
        pass

    @abstractmethod
    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front."""
        pass

    @abstractmethod
    def is_full(self) -> bool:
        """ True if the queue is full and no element can be pushed. """
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the queue."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the queue is empty. """
        return len(self) == 0

    def clear(self):
        """ Clears all elements from the queue. """
        self.length = 0