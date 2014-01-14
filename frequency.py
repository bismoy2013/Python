from collections import defaultdict
def frequency(l):
    d=defaultdict(int)
    for k in l:
        d[k]+=1
    for k in set(l):
        print(k,"occurec",d[k],"times")
