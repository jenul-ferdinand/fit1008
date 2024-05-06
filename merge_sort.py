arr = [2, 3, 2, 1, 4, 4, 5, 3 ,7, 8, 3, 2, 1, 9]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left_arr = arr[0 : len(arr) // 2]
    right_arr = arr[len(arr) // 2 : len(arr)]
    
    
