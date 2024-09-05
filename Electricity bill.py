units=int(input("Enter the number"))
if units <=100:
    a=units*5
    print("bill",a)
elif(units<=200):
    a=100*5+(units-100)*10
    print("bill",a)
elif(units>=200):
    a=100*5+100*10+(units-200)*15
    print("Bill,",a)



