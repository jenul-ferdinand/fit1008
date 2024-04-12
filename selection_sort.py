from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    for ind in range(len(arr)):
        min_index = ind
        print(f'Saved the min index ({min_index})')
        
        for j in range(ind + 1, len(arr)):
            print(f'Comparing {arr[ind]} < {arr[min_index]}')
            if arr[j] < arr[min_index]:
                print(f'current index is smaller, min_index value = {arr[j]}')
                min_index = j
            else: print(f'not smaller')
        
        print(f'Swapping {arr[ind]}, {arr[min_index]} = {arr[min_index]}, {arr[ind]}')
        print(arr)
        arr[ind], arr[min_index] = arr[min_index], arr[ind]
        print(arr)
    return arr
        
if __name__ == "__main__":
    unsorted_array = [5, 4, 3, 2, 1]
    print(f'Original array: {unsorted_array}')
    
    sorted_array = selection_sort(unsorted_array)
    print(f'Sorted array: {sorted_array}')