s=0
c=0
for i in range(int(input())):
    n,k=map(int,input().split())
    s=max(0,s-(n-c))+k
    c=n
print(s)
