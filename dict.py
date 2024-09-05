dict1={}
a=int(input("Enter the size"))
for i in range(a):
    dict2={}
    name=input("Enter the name")
    age=int(input("Enter the age:"))
    salary=int(input("Enter the salary"))
    id=int(input("Enter the id"))
    dict2["name"]=name
    dict2["age"]=age
    dict2["salary"]=salary
    dict2["id"]=id

    dict1[id]=dict2
    print(a)
    

