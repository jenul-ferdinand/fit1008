from my_stack import Stack

def mystery(s):
    sz = len(s) # -
    s2 = Stack(len(s)) # -
    s3 = Stack(len(s)) # -
    
    for _ in range(sz // 2): # O(n/2) -> O(n)
        s2.push(s.pop()) # -
    while len(s) > 0: # O(n)
        s3.push(s.pop()) # -
    while len(s2) > 0: # O(n)
        s3.push(s2.pop()) # -
    return s3

s = Stack(4)
s.push(6)
s.push(2)
s.push(7)
s.push(3)

t = mystery(s)
while(len(t) > 0): # - 
    print(t.pop())