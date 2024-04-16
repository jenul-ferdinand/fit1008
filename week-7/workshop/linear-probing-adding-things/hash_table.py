""" Hash Table ADT.

Defines a Hash Table using Linear Probing for conflict resolution.
It currently rehashes the primary cluster to handle deletion.
"""
__author__ = 'Brendon Taylor'
__docformat__ = 'reStructuredText'
__modified__ = '16/05/2020'
__since__ = '14/05/2020'

from referential_array import ArrayR
from typing import TypeVar, Generic, Callable
T = TypeVar('T')

class DeletedItem:
    pass

class LinearProbeTable(Generic[T]):
    """
    Linear Probe Hash Table

    attributes:
        count: number of elements in the hash table
        table: used to represent our table as an internal array
    """
    DEFAULT_TABLE_SIZE = 17

    def __init__(self, hash_fun: Callable[[str, int], int], table_size: int = DEFAULT_TABLE_SIZE) -> None:
        """
        :complexity: O(N) where N is the table_size
        """
        assert(table_size > 0)
        self.hash = hash_fun
        self.count = 0
        self.table = ArrayR(table_size)

    def __setitem__(self, key: str, data: T) -> None:
        """
        Set an (key, data) pair in our hash table
        :complexity: ?? assuming that N is number of elements in the table,
                     and Comp and Hash are the complexity of hashing and comparison
                     (typically linear in the size of keys)
        :raises: KeyError if the hash table is full ext free
        """
        # Find the position of the key by hashing
        pos = self.hash(key, len(self.table))

        # Find the next empty position and update the (key, data) pair 
        for i in range(len(self.table)):
            if self.table[pos] is None or self.table[pos] is DeletedItem:
                self.table[pos] = (key, data)
                self.count += 1
                return
            elif self.table[pos][0] == key:
                self.table[pos] = (key, data)
                return
            pos = (pos + 1) % len(self.table)
            
        if self.count >= len(self.table):
            raise KeyError
    
        self.table[pos] = (key, data)
        self.count += 1
        
    def __getitem__(self, key: str) -> T:
        """
        Find the data associated with a key in our hash table
        :complexity: ?? assuming that N is number of elements in the table,
                     and Comp and Hash are the complexity of hashing and comparison
                     (typically linear in the size of keys)
        :raises: KeyError if key is not in the table
        """
        pos = self.hash(key, len(self.table))
        
        for _ in range(len(self.table)):
            if self.table[pos] is None or self.table[pos] is DeletedItem:
                break
            elif self.table[pos][0] == key:
                return self.table[pos][1]
            
            # Go to the next position
            pos = (pos + 1) % len(self.table)
            
        # Raise a key error if we cannot find the key
        raise KeyError

    def __delitem__(self, key: str) -> T:
        """
        Delete the item from our hash table based on the key.

        :complexity: O(N) in the worst case, where N is the number of elements in the table,
            due to linear probing through all slots in a full table scenario.
        :raises: KeyError if key is not in the table
        """
        pos = self.hash(key, len(self.table))
        start_pos = pos
        
        while self.table[pos] is not None:
            if isinstance(self.table[pos], DeletedItem):
                pos = (pos + 1) % len(self.table)
                if pos == start_pos:
                    break
            
            if self.table[pos][0] == key:
                self.table[pos] = DeletedItem
                self.count -= 1
                return

            pos = (pos + 1) % len(self.table)
            if pos == start_pos:
                break
            
        raise KeyError("Key not found: " + str(key))