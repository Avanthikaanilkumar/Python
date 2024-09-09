num=int(input("Enter the no of elements"))
a=[]
print("Enter the elements:")
for i in range(num):
    b=int(input())
    a.append(b)
for i in range(num):
    for j in range(i,num):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("second largest element is:",a[num-2])

       