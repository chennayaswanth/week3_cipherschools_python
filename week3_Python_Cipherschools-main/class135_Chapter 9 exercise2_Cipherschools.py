#list--->[True,False,[1,2,3],1,1.0,3]
#output--->["1","1.0","3"]

list1=[True,False,[1,2,3],1,1.0,3]
list2=[str(i) for i in list1 if type(i)==int or type(i)==float]
print(list2)