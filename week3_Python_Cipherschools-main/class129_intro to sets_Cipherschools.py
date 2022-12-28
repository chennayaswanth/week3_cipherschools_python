#remove duplicate using sets
l=[1,2,3,3,4,2,4,5,5,6,7,7,7,8,9,8]
print(list(set(l)))

#changing in sets
s={1,2,3,4,5}
s.add(7)
s.remove(3)
s.discard(2)
print(s)