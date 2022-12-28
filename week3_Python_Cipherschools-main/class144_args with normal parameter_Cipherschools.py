# Normal parameters should only come before *args

def mul(num,*args):
    mul = 1
    for i in args:
        mul *= i
    return mul

print(mul(2,5,6,7,3,45,6,6))  # 2 will not be get multiplied as it will not be considerd within args