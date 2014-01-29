s=input("Enter the string : ")
d=list(s)
array=[]
a=[]
ind=[]
print("STRUCTURE")
print("...................................")
for i in range(len(s)):
    print(''.join(d))
    array.append(''.join(d))
    del(d[0])
print("...................................")
a=sorted(array)
print("Array: ",array)
print("Sorted Array: ",a)
for i in range(len(a)):
    print((a[i]),'--> ',array.index(a[i]))
    ind.append(array.index(a[i]))
print(ind)
