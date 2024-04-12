from aset import ASet

# After defining and and or, read the files and add them to each set
# Then test the operations if our AND and OR works 

# Open and store the files
with open('giant_list_1.txt') as file:
    list1 = file.read().split('\n')

with open('giant_list_2.txt') as file: 
    list2 = file.read().split('\n')

# Trim the empty whitespacke from the end 
list1 = list1[:-1]
list2 = list2[:-1]

# Initialise the sets
set1 = ASet(len(list1))
set2 = ASet(len(list2))

# Add the items from the lists to the sets
for item in list1:
    set1.add(item)

for item in list2:
    set2.add(item)

# Perform a bitwise and operation to find the common values
print(set1 & set2)
