import math
d=[]
for a in range(3,int(1e5),2):
    b=((a*a)-1)//2
    if b*b+a*a==(b+1)*(b+1):
        d.append(b+1)
for i in range(int(input())):
    n=int(input())
    l=0
    h=len(d)-1
    while l<=h:
        m=(h+l)//2
        if d[m]>n:
            h=m-1
        if d[m]<=n:
            l=m+1
    print(l)                    