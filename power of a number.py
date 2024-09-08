x=int(input("Enter the base:"))
y=int(input("Enter the exponent:"))
result=1
for i in range(y):
    result=result*x
print(f"{x} raised to the power of {y} is {result}")
