import random
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    random.shuffle(a)
    if len(set(a))==1:
        print(0)
    else:
        d={}
        m=0
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            m=max(m,d[i])    
        c=n-m
        while m<n:
            m=m*2
            c+=1
        print(c)            
                                