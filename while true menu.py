students={}
i=1
while True:
    print("1.Registration \n 2.Display\n 3.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        d={}
        a=input("Enter the name:")
        b=input("Enter the age:")
        c=input("Enter the address:")
        d["name"]=a
        d["age"]=b
        d["address"]=c
        students[i]=d
        i=i+1
        print(students)
    elif choice==2:
        flag=0
        e=input("Enter the name to search:")
        for name in students:
            if  students[name]["name"]==e:
                print("Name : ",students[name]["name"])
                print("Age:",students[name]["age"])
                print("Address:",students[name]["address"])

                flag=1
                break
        if flag==0:
            print("Not found")
            
    elif choice==3:
        print("Exit")
        break
               












        







