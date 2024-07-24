from typing import List, Optional
import random
from swap import swap

def quick_sort(array) -> List:
    """
    :complexity best: O((n * log(n)) * comp=), When we pick median as the pivot.
    :complexity worst: O((n^2) * comp=), When we pick min/max as pivot.
    """
    random.seed()
    
    low = 0
    high = len(array) - 1
    quick_sort_aux(array, low, high)
        
def quick_sort_aux(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort_aux(array, low, pivot - 1)
        quick_sort_aux(array, pivot + 1, high)
        
def partition(array, low, high, pivot : Optional[int] = None):
    """
    Randomly selects a pivot element and
    1. Moves smaller elements to the left
    2. Moves greater elements to the right
    Returns the position of the pivot element
    
    :returns: The position of the pivot element.
    """
    # Pick a random pivot 
    if pivot is None: pivot = random.choice(range(low, high+1))
    # Make sure the pivot is within bounds
    else: assert(low <= pivot <= high)
    
    # Swapping the pivot with the first element
    array[low], array[pivot] = array[pivot], array[low]
    print(array)
    
    # Traversing all the elements
    boundary = low
    for i in range(low + 1, high + 1):
        # If the current element is smaller than or equal to the pivot
        # (currently stored in position low)
        if array[i] <= array[low]:
            boundary += 1
            # Move the smaller element to the left part
            array[i], array[boundary] = array[boundary], array[i]
            print(f'Element {i}: {array}')
    # Moving the pivot back to its position
    array[low], array[boundary] = array[boundary], array[low]
    print(f'Swapping pivot: {array}')
    # Return the position of the pivot element
    return boundary

if __name__ == '__main__':
    arr = [6, 5, 4, 3, 2, 1]
    quick_sort(arr)
    print(arr)