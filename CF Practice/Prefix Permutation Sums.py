for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = set(list(range(1, n + 1)))
    d=0
    t=((n*(n+1))//2)
    if max(a)>t:
        print("NO")
        continue
    if a[0]<=n:
        l.remove(a[0])
    else:
        d+=a[0]    
    for i in range(1, n-1):
        if a[i] - a[i - 1] in l:
            l.remove(a[i] - a[i - 1])
        else:
            d = a[i] - a[i - 1]
    if sum(l) == d or max(a)+sum(l)==t:
        print("YES")
    else:
        print("NO")
