import random

def higher_or_lower(target: int) -> str:
    """ Higher or lower game
    
    :param target: The chosen integer to win game
    :complexity: O(n) where n is the target integer
    """
    
    x = int(input("Type a integer: "))
    try:
        if x > target:
            return "Go lower"
        if x < target:
            return "Go higher"
        else:
            return "Nice!"
    except ValueError:
        return "Enter a number (integer)"

if __name__ == '__main__':
    target = random.randint(0,1000)
    print(higher_or_lower(target))