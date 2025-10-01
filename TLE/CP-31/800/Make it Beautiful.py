for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a.count(a[0])==n:
        print("NO")
    elif len(set(a))==len(a):
        print("YES")
        print(*sorted(a,reverse=True))    
    else:
        a.sort(reverse=True)
        f=0
        s=0
        for i in range(n):
            if s==a[i]:
                f=1
                break
            s+=a[i]
        if f:
            a[0],a[-1]=a[-1],a[0]
        print("YES")    
        print(*a)  





