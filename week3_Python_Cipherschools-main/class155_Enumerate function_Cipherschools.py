# We use enumerate function with for loop to track position of ot

# item in iterable

# How we can do this without enumerate function
names = ['abc', 'abcdef', 'harshit']
#@ "abc"
#1 "abcdef"
pos = 0
for name in names:
    print(f"{pos} ----> {name}")
    pos += 1

# with enumerate function
for pos, name in enumerate(names):
    print(f"{pos} ----> {name}")

# Define a function that rake! two arguments

# 1.) list containing string

# 2.) string that want to find in your list

# and this function will return the index of string in your list and
# if string is not present then return -1
def find_pos(l, target):
    for pos, name in enumerate(1):
        if name == target:
            return pos
    return -1

print (find_pos(names, 'abcz'))