# Set Comprehension 

square = {i**2 for i in range(3,12)}
print(square)

cube = {i**3 for i in range(7,23) if i%2==0}
print(cube)

odd_even = {i if i%2==0 else -i for i in range(45,55)}
print(odd_even)