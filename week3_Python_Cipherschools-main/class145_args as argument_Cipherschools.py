# Function to print product of given numbers by user

def multiply(*args):
    mul = 1
    for i in args:
        mul *= i
    return mul

num = list(map(int,input('Enter numbers: ').split(',')))
print(multiply(*num))