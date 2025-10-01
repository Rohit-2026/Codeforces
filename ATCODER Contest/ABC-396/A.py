n=int(input())
a=list(map(int,input().split()))
f=0
for i in range(n-2):
    if a[i]==a[i+1] and a[i+1]==a[i+2]:
        print("Yes")
        f=1
        break
if f==0:
    print("No")    