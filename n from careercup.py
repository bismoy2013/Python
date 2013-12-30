#Given n. Generate all numbers with number of digits equal to n, such that the digit to the right is greater than the left digit (ai+1 > ai). E.g. if n=3 (123,124,125,……129,234,…..789)
import math
def function(n):
    count=0
    while(n>0):
        f=n%10
        g=(n%100)/10
        if(f>g):
            count=count+1
        n=n//10
    return (count)
a=int(input("Enter the no of digits: "))
for i in range(pow(10,a-1),pow(10,a)):
    if(function(i)==a):
       print(i)
