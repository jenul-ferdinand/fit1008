from data_structures.stack_adt import ArrayStack

string = '()()'
stack = ArrayStack(len(string))

for char in string:
    stack.push(char)

open_count = 0
close_count = 0
for char in string:
    item = stack.pop()
    if item == '(':
        open_count += 1
    if item == ')':
        close_count += 1 

if open_count == close_count:
    print('Balanced')
else: 
    print('Unbalanced')