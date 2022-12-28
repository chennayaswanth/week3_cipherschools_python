# Function to print powers of given number

def power(num,*args):
    l = [i**num for i in args]
    return l

num = int(input("Enter power: "))
try:
    nums = [int(i) for i in input("Enter numbers: ").split(',')]
except ValueError:
    nums = []

if len(nums)==0:
    print("Hey! you didn't pass any number")
else:
    print(power(num,*nums))