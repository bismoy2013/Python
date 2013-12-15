def convert(n):
    ones=['zero','one','two','three','four','five','six','seven','eight','nine']
    twos=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    ts=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    big=['hundred','thousand','lac','million']
    if(len(str(n))==1):
        print(ones[n])
    elif(len(str(n))==2 and n%10==0):
        y=n//10
        print(twos[y-1])
    elif(len(str(n))==2 and n%10!=0 and n<20):
        y=n%10
        print(ts[y-1])
    elif(len(str(n))==2 and n%10!=0 and n>20):
        y=n//10
        z=n%10
        print(twos[y-1].capitalize()+' '+ones[z])
    elif(len(str(n))==3):
        if(n%100==0):
            y=n//100
            print(ones[y]+' '+big[0])
        else:
            y=n//100
            print(ones[y].capitalize()+' '+big[0]+' and',end=' ')
            convert(n%100)
    elif(len(str(n))==4):
        if(n%1000==0):
            y=n//1000
            print(ones[y].capitalize()+' '+big[1])
        else:
           y=n//1000
           print(ones[y].capitalize()+' '+big[1]+' ',end=' ')
           convert(n%1000)
    elif(len(str(n))==5):
        y=n//1000
        if(y%10==0):
            g=y//10
            print(twos[g-1].capitalize()+' '+big[1]+' ',end='')
        elif(y%10!=0 and y<20):
            g=y%10
            print(ts[g-1].capitalize()+' '+big[1]+' ',end='')
        elif(y%10!=0 and y>20):
            g=y//10
            h=y%10
            print(twos[g-1].capitalize()+' '+ones[h]+' '+big[1]+'',end=' ')
        convert(n%1000)
    elif(len(str(n))==6):
        if(n%100000==0):
            y=n//100000
            print(ones[y].capitalize()+' '+big[2])
        else:
            y=n//100000
            print(ones[y].capitalize()+' '+big[2]+'',end=' ')
            convert(n%100000)
    elif(len(str(n))==7):
        if(n%1000000==0):
            y=n//1000000
            print(ones[y].capitalize()+' '+big[3])
        else:
            y=n//1000000
            print(ones[y].capitalize()+' '+big[3]+'',end=' ')
            convert(n%1000000)
    else:
        print("We dint cover number of that much digits, I mean beyond million!")
