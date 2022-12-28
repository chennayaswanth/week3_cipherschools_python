# define a function which returns dict with cube till numbers
#{1:1,2:4,3:9}
def cube(a):
    d={}
    for i in range(1,a+1):
        d[i]=i**2
    return d
a=int(input("Enter a number: "))
print(cube(a))