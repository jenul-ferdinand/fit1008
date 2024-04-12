from StackADT import Stack

def is_balanced(some_string: str) -> bool:
    """ Checks if parathensis are matching in a string 
    
    :complexity: In the worst-case O(n), in the best-cause, O(1)
    """

    stack = Stack(len(some_string))

    for ch in some_string:
        if ch == '(' or ch == '[' or ch == '{':
            stack.push(ch)
        elif (stack.is_empty() 
            or ch == ')' and stack.peek() != '('
            or ch == ']' and stack.peek() != '['
            or ch == '}' and stack.peek() != '{'):

            return False
        else:
            stack.pop()
    return stack.is_empty()

def is_balanced2(some_string: str) -> bool:
    """ Checks if parathensis are matching in a string 
    
    :complexity: In the worst-case O(n), in the best-cause, O(1)
    """

    stack = Stack(len(some_string))

    for ch in some_string:
        if ch == '(':
            stack.push(ch)
        elif ch == ')':
            if stack.is_empty():
                return False

            if stack.pop() != '(':
                return False
            
        return stack.is_empty()

def is_balanced3(some_string: str) -> bool: 
    stack = Stack(len(some_string))
    
    open_chars = "({["
    close_chars = ")}]"
    
    for char in some_string:
        if char in open_chars:
            stack.push(char)
        elif char in close_chars:
            if stack.is_empty():
                return False
            last = stack.pop()
            if open_chars.index(last) == close_chars.index(chars): 
                return False
            
    return stack.is_empty()
            

if __name__ == '__main__':
    print(is_balanced('()[}'))


"""Alternatively describe your implementation here: 
First initialise the Stack
Loop through the characters in the string
    IF the current char is a '('
        Push the current char to the stack
    ELSE IF check if the stack is empty OR the current char is ')' 
    AND peek the stack and check if the top char is NOT '('
        RETURN False
    ELSE 
        Pop the top char in the Stack
RETURN stack is empty

"""


