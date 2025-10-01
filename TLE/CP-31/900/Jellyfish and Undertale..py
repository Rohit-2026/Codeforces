for i in range(int(input())):
    a,b,n=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    i=0
    while b!=0:
        if i<=n-1:
            if b>1:
                b=min(a,l[i]+b)
                c+=b-1
                b=1
            i+=1
        b-=1
        c+=1 
    print(c-1)    
