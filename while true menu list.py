students=[]
i=1
while True:
    print("1.Registration \n 2.Display\n 3.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        d=[]
        a=input("Enter the name:")
        d.append(a)
        b=input("Enter the age:")
        d.append(b)
        c=input("Enter the address:")
        d.append(c)
        students.append(d)        
        
        print(students)
    elif choice==2:
        flag=0
        e=input("Enter the name to search:")
        for x in students:
                if x[0]==e:
                     print("name:",x[0])
                     print("Age:",x[1])
                     print("Address:",x[2])
                     
                flag=1
                break
        if flag==0:
            print("Not found")
            
    elif choice==3:
        print("Exit")
        break
               












        







