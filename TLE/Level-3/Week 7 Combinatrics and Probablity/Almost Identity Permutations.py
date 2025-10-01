n,k=map(int,input().split())
c=0
if k==1:
    print(1)
else:
    for i in range(2,k+1):
        if i==2:
            c+=(n*(n-1))//2
        elif i==3:
            c+=(n*(n-1)*(n-2))//3
        elif i==4:
            c+=(n*(n-1)*(n-2)*(n-3))//24*9      
    print(c+1)        