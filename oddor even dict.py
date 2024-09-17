# {"13579":"246810"}
odd=""
even=""
for i in range(1,11):
    if i%2==0:
        even=even+str(i)
    else:
        odd=odd+str(i)
print("{"  + odd + ":" +even + "}")



