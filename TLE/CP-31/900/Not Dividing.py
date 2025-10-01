for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]==1:
        a[0]+=1
    for i in range(1,n):
        if a[i]%2==a[i-1]%2:
            if (a[i]+1)%a[i-1]==0:
                a[i]+=2
            else:
                a[i]+=1            
    print(*a)               