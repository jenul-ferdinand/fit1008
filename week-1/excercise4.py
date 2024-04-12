def get_digital_root(n: int) -> int:
    n = str(n)
    
    while len(n) > 1:
        digit_sum = sum(int(digit) for digit in n)
        
        n = str(digit_sum)
        
    return int(n)
        

if __name__ == '__main__':
    number = 979853562951413
    print(get_digital_root(number))