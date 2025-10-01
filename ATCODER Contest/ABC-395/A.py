n=int(input())
a=list(map(int,input().split()))
f=0
for i in range(1,n):
    if a[i]<=a[i-1]:
        f=1
        break
if f==1:
    print("No")
else:
    print("Yes")
            