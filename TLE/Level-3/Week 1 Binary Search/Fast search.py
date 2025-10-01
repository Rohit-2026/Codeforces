from bisect import bisect_left, bisect_right
n=int(input())
a=list(map(int,input().split()))
a.sort()
t=[]
for i in range(int(input())):
    p,q=map(int,input().split())
    l=bisect_left(a,p)
    r=bisect_right(a,q)
    t.append(r-l)
print(*t)
