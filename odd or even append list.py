a=[]
b=[]
c=[]
for i in range(0,10):
    if i%2==0:
        b.append(i)
    else:
        a.append(i)        
print(a)
print(b)
c.append(a)
c.append(b)
print(c)
