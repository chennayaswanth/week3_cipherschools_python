def word(name):
    d={}
    for i in name:
        d[i]=name.count(i)
    return d
name=input("Enter your name: ")
print(word(name))