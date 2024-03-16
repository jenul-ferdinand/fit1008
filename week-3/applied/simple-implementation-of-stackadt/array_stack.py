from stack_adt import Stack
from referential_array import ArrayR
from typing import TypeVar

T = TypeVar('T')

class ArrayStack(Stack):
    def __init__(self, capacity) -> None:
        Stack.__init__(self)
        self.array = ArrayR(capacity)
        self.top = -1
        
    def push(self, item:T) -> None:
        """ Pushes an element to the top of the stack."""
        if self.is_full():
            raise Exception("Stack is full")
        
        self.top += 1
        self.array[self.top] = item

    def pop(self) -> T:
        """ Pops an element from the top of the stack."""
        if self.is_empty():
            raise Exception("Tried to pop from an empty stack")
        
        element = self.array[self.top]
        self.top -= 1
        return element

    def peek(self) -> T:
        """ Pops the element at the top of the stack."""
        if self.is_empty():
            raise Exception("Attempted to peek an empty stack")
        return self.array[self.top]

    def __len__(self) -> int:
        """ Returns the number of elements in the stack."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the stack is empty. """
        return len(self) == 0

    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        return self.top+1 >= len(self.array)

    def clear(self):
        """ Clears all elements from the stack. """
        self.length = 0
