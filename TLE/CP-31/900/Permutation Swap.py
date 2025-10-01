import math
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=[]
    c=0
    for i in range(n):
        if a[i]-i-1!=0:
            t.append(abs(a[i]-i-1))
    for i in t:
        c=math.gcd(c,i)
    print(c)    