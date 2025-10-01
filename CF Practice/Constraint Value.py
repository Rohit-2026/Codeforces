for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    for i in range(1,n):
        if abs(a[i]-a[i-1])>=m:
            m=abs(a[i]-a[i-1])
