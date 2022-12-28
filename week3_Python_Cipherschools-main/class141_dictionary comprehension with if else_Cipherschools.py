# Dictionary Comprehension 

cube = {i:i**3 for i in range(0,11)}
print(cube)

odd = {i:'odd' for i in range(0,11) if i%2==1}
print(odd)

odd_even = {i:('odd' if i%2==1 else 'even') for i in range(80,99)}
print(odd_even)