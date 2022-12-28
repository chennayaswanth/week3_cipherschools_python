d={}
name=input("Enter your name: ")
age=int(input("What is your age?: "))
movies=input("Enter fav movies sep by commas: ").split(",")
songs=input("Enter fav songs sep by commas: ").split(",")
d['name']=name
d['age']=age
d['Fav-movies']=movies
d['Fav-songs']=songs
for key,value in d.items():
    print(key,"->",value)