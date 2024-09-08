ele= []
n=int(input("Enter the number of elements:"))
for i in range(n):
    a=int(input("Enter the elements:"))
    ele.append(a)
freq = {}
for i in ele:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print("The frequency is:",freq)