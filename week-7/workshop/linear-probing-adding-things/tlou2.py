from hash import simple_hash, better_hash
from hash_table import *

characters = ('Joel', 'Owen', 'Meg', 'Manny', 'Tommy', 'Jesse', 'Abby', 'Ellie')

if __name__ == '__main__':
    table = LinearProbeTable(simple_hash)

    print('adding words')
    for word in characters:
        table[word] = True
    
    print('checking table\'s contents')
    for slot in range(len(table.table)):
        print('table[{0}] = {1}'.format(slot, table.table[slot]))

    print('are there collisions?')
    for word in characters:
        print('hash[\'{0}\'] = {1}'.format(word, table.hash(word)))