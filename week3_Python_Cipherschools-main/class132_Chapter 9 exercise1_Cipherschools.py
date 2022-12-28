#input list with strings
#create a another list using list comprehension in which inputs will be reversed

l1=input("Enter names sep by comma: ").split(",")
l2=[[name[::-1] for name in  l1]]
print(l2)