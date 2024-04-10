from typing import List

def bubble_sort(array: List[int]) -> List[int]:
    temp = None
    
    # Loop for traversing the list
    for _ in range(len(array)):
        
        # This inner loop traverses the list from start to the second last
        # element and does the comparisons and swapping.
        for j in range(len(array) - 1):
            
            # Check if the current item is greater than the next item
            if array[j] > array[j + 1]:
                
                # Store the current item in a temp variable
                temp = array[j]
                
                # Swap the position of the next item 
                # to the position of the current item
                array[j] = array[j + 1]
                
                # Now set the next positions item to the larger item
                array[j + 1] = temp
                
    # Return the sorted list
    return array

if __name__ == "__main__":
    array = [5, 4, 3, 2, 1]
    print(f"Original Array: {array}")
    
    array = bubble_sort(array)
    print(f"Sorted Array: {array}")