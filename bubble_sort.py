from typing import List

def bubble_sort(array: List[int]) -> List[int]:
    for i in range(len(array)):
        print(f'\n======== ITERATION i={i} ========')
        for j in range(len(array) - 1):
            print(f'\nj={j} === COMPARING {array[j]} > {array[j+1]} ===')
            if array[j] > array[j + 1]:
                print(f'{array}')
                print(f'Swapping item at {j} ({array[j]}) with item at {j+1} ({array[j+1]})')
                array[j], array[j+1] = array[j+1], array[j]
                print(array)
            else:
                print(f'array[{j}] smaller than array[{j+1}]')
    return array

def improved_bubble_sort(array: List[int]) -> List[int]:
    n = len(array)
    for mark in range(n-1, 0, -1):
        for i in range(mark):
            if (array[i] > array[i + 1]):
                array[i], array[i+1] = array[i + 1], array[i]
    return array

if __name__ == "__main__":
    array = [-5, -20, -5, -10, 3]
    print(f"Original Array: {array}")
    
    array = bubble_sort(array)
    print(f"\nSorted Array: {array}")