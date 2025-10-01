n,m=map(int,input().split())
b=sorted(map(int,input().split()))
w=sorted(map(int,input().split()))
s=0
while w and b and w[-1]+b[-1]>-1 and w[-1]>-1:
    s+=w.pop()+b.pop()
while b and b[-1]>-1:
    s+=b.pop()
print(max(s, 0))