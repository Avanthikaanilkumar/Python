a=set() #empty set
print(type(a))
set1={1,6,4,'abc'}
print(type(set1))
Days=set(["Monday","Tuesday","Wednesday","Thursday"])#set method
print(Days)
print(type(Days))
for i in Days:
    print(i)
Months=set(["January","February","March"])#add method
print(Months)
Months.add("July")
print(Months)
Months=set(["January","February","March"])#update
print(Months)
Months.update(["July","August"])
print(Months)
Months=set(["january","February","March"])
print(Months)
Months.discard("january")#DISCARD
print(Months)
Months=set(["january","February","March","April"])#remove
print(Months)
Months.remove("january")
print(Months)
Days1={"Monday","Tuesday","Wednesdsay"}
Days2={"Friday","Saturday","Sunday"}
print(Days1|Days2)
Days1={"Monday","Tuesday","Wednesday","Thursday"}
Days2={"Monday","Tuesday","Sunday","Friday"}
print(Days1&Days2)
Days1={"Monday","Tuesday","Wednesday","Thursday"}
Days2={"Monday","Tuesday"}
Days3={"Monday","Tuesday","Friday"}
print(Days1>Days2)
print(Days1<Days2)
print(Days2==Days3)



