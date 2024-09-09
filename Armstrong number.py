n=int(input("Enter the number:"))
temp=n
sum=0
length=len(str(n))
while temp>0:
    digit=temp%10
    sum=sum + digit**length
    temp=temp//10
if sum==n:
   print("It is an Armstrong number")
else:
   print("It is not an Armstrong number")


