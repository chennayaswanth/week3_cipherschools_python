#given [1,2,3,4,5,6,7,8,9,10]
#output [-1,4,-3,8,-5,-----]
l=[1,2,3,4,5,6,7,8,9,10]
new=[i*2 if i%2==0 else -i for i in l]
print(new)