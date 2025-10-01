import math
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=0
    for i in range(1,n):
        if a[i-1]>a[i]:
            print(0)
            t=1
            break
    if t==0:
        c=1000000000
        for i in range(1,n):
            c=min(c,a[i]-a[i-1])
        if c==0:
            print(1)
        elif c%2==0:
            print(math.ceil(c/2)+1)
        else:
            print(math.ceil(c/2))        

