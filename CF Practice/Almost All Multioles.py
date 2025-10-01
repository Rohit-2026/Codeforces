for i in range(int(input())):
    n,x=map(int,input().split())
    if n%x:
        print(-1)
        continue
    else:
        a=[]
        for i in range(2,n):
            a.append(i)
        a.append(1)
        a=[n]+a
        if n==x:
            print(*a)
        else:
            a[0]=x
            a[x-1]=n
            t=x
            for i in range(t,n-1):
                if n%a[i]==0 and a[i]%t==0:
                    a[t-1],a[i]=a[i],a[t-1]
                    t=i+1        
            print(*a)

