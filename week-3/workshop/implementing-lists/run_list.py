from array_list import *

if __name__ == '__main__':
    l = ArrayList(8)
    print('list capacity is set to 8')
    print('the list is initially empty:')
    print(l)

    print('')
    for i in range(1, 5):
        print('appending item', i)
        l.append(i)

    print('')
    print('list contents:')
    print(l)
    print('list\'s array contents:')
    arr = [l.array[i] for i in range(len(l.array))]
    print(arr)

    print('')
    print('removing item', 2)
    l.remove(2)
    print('deleting item (3) at index 1')
    l.delete_at_index(1)
    print('inserting item', 5, 'at index', 0)
    l.insert(0, 5)
    print('appending item', 6)
    l.append(6)

    print('')
    print('list contents:')
    print(l)
    print('list\'s array contents:')
    arr = [l.array[i] for i in range(len(l.array))]
    print(arr)

    for i, j in enumerate((7, 8, 9)):
        print('inserting item', j, 'at index', 2 * i + 1)
        l.insert(2 * i + 1, j)

    print('')
    print('list contents:')
    print(l)
    print('list\'s array contents:')
    arr = [l.array[i] for i in range(len(l.array))]
    print(arr)