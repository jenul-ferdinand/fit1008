from QueueADT import CircularQueue
from StackADT import Stack 

def reverse_queue(my_queue: CircularQueue) -> CircularQueue: 
    result_queue = CircularQueue(len(my_queue))
    my_stack = Stack(len(my_queue))

    for _ in range(len(my_queue)):
        
        item = my_queue.serve()
        
        if item != '':
            my_stack.push(item)
        my_queue.append(item)

    while not my_stack.is_empty():
        item = my_stack.pop()
        result_queue.append(item)

    return result_queue 

my_queue = CircularQueue(5)
my_queue.append("Hello")
my_queue.append("Goodbye")
my_queue.append("Not now")
my_queue.append("")
my_queue.append("Later")
result_queue = reverse_queue(my_queue)
print(my_queue)
print(result_queue)

"""Alternatively describe such an algorithm which does this here: 

Take (serve) each string from the queue and push it into the stack (if not empty)
- As we serve element we should papend them back to the end of the original queue

Take (pop) each string from the stack and pop it into the new queue 

Return the new queue




"""