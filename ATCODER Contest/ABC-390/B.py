n=int(input())
a=list(map(int,input().split()))
if n==2:
    print("Yes")
else:
    f=0
    t=a[1]/a[0]
    for i in range(1,n-1):
        if a[i]*t!=a[i+1]:
            f=1
            break 
    if f:
        print("No")
    else:
        print("Yes")        