import random
from typing import List

def search_number(li: List[int], targ: int) -> bool:
    """ Linear search
    :complexity: O(n) Where n is the length of the list
    """
    
    for integer in li:
        if integer == targ:
            return True
    
    return False
        
def binary_search(li: List[int], targ: int) -> bool:
    """ Binary search
    :complexity: O(logn) Where n is the length of the list
    """
    
    left = 0            # Initialise at start of the list
    right = len(li) - 1 # Initialise at end of the list
    
    while left <= right:
        mid = left + (right - left) // 2 # Middle of left and right
        if li[mid] == target: 
            return True 
        elif li[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
            
    return False
    
if __name__ == '__main__':
    # Create a random sorted list
    randomlist = random.sample(range(0, 100), 10)
    randomlist.sort()
    
    # Debugging
    print(randomlist)
    
    # Ask the user for the target integer
    target = int(input("What integer are you looking for? "))
    
    # Normal search method O(n)
    print(search_number(randomlist, target))
    
    # Binary search method O(logn)
    print(binary_search(randomlist, target))