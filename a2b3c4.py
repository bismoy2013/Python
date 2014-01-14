s=input("Enter string: ")
store=[]
num=[]
su=0
k=0
print(len(s))
for i in range(len(s)):
    if((s[i].isdigit()==False)):
        store.append(s[i])
        if(k!=0):
            num.append(su)
        k=0
        su=0
    else:
        su=su*10+int(s[i])
        k=k+1
        if(i+1==len(s)):
            num.append(su)
    
print(store) #You can keep track of the array where I am storing the contents from the given string
print(num)
for i in range(len(store)):
    print(store[i]*num[i],end='')
