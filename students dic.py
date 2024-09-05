students=[]
a=int(input("Enter the number of students:"))
id=0
for i in range(a):
    dictionary={"ID":"","Name":"","Age":"","Marks":""}
    name=input("Enter the name of student: ")
    age=input("Enter the age: ")
    mark1=int(input("Mark of subject 1: "))
    mark2=int(input("Mark of subject 2: "))
    mark3=int(input("Mark of subject 3: "))
    id=id+1
    dictionary["ID"]=id
    dictionary["Name"]=name
    dictionary["Age"]=age
    dictionary["Marks"]=[mark1,mark2,mark3]
    students.append(dictionary)
   
print(students)
 


    















