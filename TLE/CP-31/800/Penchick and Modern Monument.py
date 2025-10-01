for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    c=0
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1    
    for i in d:
        c=max(c,d[i])    
    print(n-c)        