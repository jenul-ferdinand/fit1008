from typing import TypeVar
from circular_queue import CircularQueue

T = TypeVar('T')

def hot_potato(queue, num) -> str:
    while len(queue) > 1:
        for _ in range(num):
            queue.append(queue.serve())
        num -= 1
        queue.serve()
        
    return queue.serve()

if __name__ == "__main__":
    q = CircularQueue(4)
    q.append("Johnny")
    q.append("Rebecca")
    q.append("Aidan")
    q.append("Smith")
    
    print(f"The winner is {hot_potato(q, 5)}")
    
    