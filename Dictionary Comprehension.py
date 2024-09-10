a="ABA"
dic = {x: {y: x + y for y in a} for x in a} 
print(dic) #Nested list comprehension

a = {x: x**2 for x in [1,2,3,4,5]}
print (a)

a = {x.upper(): x*3 for x in 'coding '}
print (a) #Dictionary comprehension

newdict={x: x**3 for x in range(10) if x**3 % 4==0}
print(newdict)





