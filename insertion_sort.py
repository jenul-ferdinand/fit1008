from typing import List

def insertion_sort(array: List[int]) -> List[int]:
    n = len(array)
    for mark in range(1, n):
        temp = array[mark]
        print(f'\nCurrent element (temp) at index {mark}: {temp}')

        i = mark - 1  # Start comparing with the element just before the current element
        while i >= 0 and array[i] > temp:  # Move elements of array[0..i-1], that are greater than temp, to one position ahead of their current position
            array[i+1] = array[i]  # Shifting the element to the right
            print(f'Shifting {array[i]} right to index {i+1}')
            i -= 1  # Move to the next element on the left

        # Insert the temp (current element being sorted) at its correct position
        print(f'Inserting temp value {temp} into its correct position at index {i+1}')
        array[i+1] = temp
        print(f'Array after inserting {temp} into its position: {array}')
    return array

if __name__ == "__main__":
    unsorted_list = [-7,-1,-4,4,5,6]
    print(f'Unsorted List: {unsorted_list}')
    sorted_list = insertion_sort(unsorted_list)
    print(f'Sorted List: {sorted_list}')