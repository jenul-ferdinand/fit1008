from aset import ASet

# After defining and and or, read the files and add them to each set
# Then test the operations if our AND and OR works 

with open('giant_list_1.txt') as f:
    lines = f.readlines()
    set1 = ASet(len(lines))
    
    for line in lines:
        set1.add(lines)
        
with open('giant_list_2.txt') as f:
    lines = f.readlines()
    set2 = ASet(len(lines))
    
    for line in lines:
        set2.add(lines)
        
