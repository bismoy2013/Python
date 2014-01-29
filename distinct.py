def distinct_pairs(A):
    count=0
    k=int(input("Difference equal to : "))
    for i in range(len(A)):
        if(A[i]+k in A):
            count=count+1
        else:
            count=count
    print("Count: ",count)



