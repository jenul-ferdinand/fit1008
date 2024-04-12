from circular_queue import *

if __name__ == '__main__':
    q = CircularQueue(5)
    print('queue capacity is set to 5')
    print('the queue is initially empty:')
    print(q)

    print('')
    print('adding item', 1)
    q.append(1)
    print('adding item', 2)
    q.append(2)
    print('adding item', 3)
    q.append(3)
    print('adding item', 4)
    q.append(4)

    print('')
    print('queue contents:')
    print(q)
    print('queue\'s array contents:')
    arr = [q.array[i] for i in range(len(q.array))]
    print(arr)

    print('')
    print('serving an item', q.serve())
    print('serving an item', q.serve())
    print('adding item', 5)
    q.append(5)
    print('adding item', 6)
    q.append(6)

    print('')
    print('queue contents:')
    print(q)
    print('queue\'s array contents:')
    arr = [q.array[i] for i in range(len(q.array))]
    print(arr)