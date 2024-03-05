import math

def good(n: int):
    """
    
    :complexity: 
    """
    
    size = 0 # 1
    output = [0] * (1 + int(math.log10(n))) # 1
    while n >= 1: # n
        output[size] = n % 10 # 1
        size += 1 # 1
        n = n // 10  # 1
    for i in range(size - 1, -1, -1) : # 1
        print(output[i], end='') # 1
    print() # 1
    
    # This function has a complexity of n 

good(9876)