from typing import List

def merge_sort(arr: List) -> List:
    if len(arr) <= 1:
        return arr

    left_arr = arr[0 : len(arr) // 2]
    right_arr = arr[len(arr) // 2 : len(arr)]
    
    merge_sort(left_arr)
    merge_sort(right_arr)
    
    i = 0 # left_arr index
    j = 0 # right_arr index
    k = 0 # merged array index
    
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1 
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr): 
        arr[k] = right_arr[j]
        j += 1
        k += 1
        
    return arr
    
if __name__ == '__main__':
    arr = [2, 3, 2, 1, 4, 4, 5, 3 ,7, 8, 3, 2, 1, 9]
    print(merge_sort(arr))