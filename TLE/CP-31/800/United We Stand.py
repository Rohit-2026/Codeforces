for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    c=[]
    for i in range(n):
        if a[i]%2==0:
            b.append(a[i])
        else:
            c.append(a[i])
    if a.count(a[0])==n:
        print(-1)
    elif not b or not c:
        a.sort()
        k=a.count(a[-1])
        print(n-k,k)
        print(*a[0:-k])
        print(*a[-k:])    
    else:
        print(len(c),len(b))
        print(*c)
        print(*b)                