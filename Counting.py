#Counting Sort
def find_max(A):
    m=A[0]
    for i in range(len(A)):
        if(A[i]>m):
            m=A[i]
        else:
            m=m
    return m
def real_sort(B):
    maxx=find_max(B)
    print(maxx)
    arr=[]
    count=[]
    for i in range(maxx+1):
        arr.append(0)
    for i in range(len(B)):
        x=B[i]
        arr[x]=arr[x]+1
    for i in range(len(arr)):
        if(arr[i]>=1):
            for j in range(arr[i]):
                count.append(i)
    print(count)
