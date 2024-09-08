a=int(input("Enter the number:"))
if a<=1:
    print("It is not prime number")
for i in range(2,a):
    if(a%i==0):
        print("it is not prime number",a)
        break
    else:
        print("it is prime number",a)
    

