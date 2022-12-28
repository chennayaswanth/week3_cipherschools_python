# Function to return sum of given input using args

def sums(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sums(1,2,5,4,6,8,6,7))