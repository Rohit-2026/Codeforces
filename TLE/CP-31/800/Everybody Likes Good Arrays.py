for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(1,n):
        if a[i]%2==a[i-1]%2:
            c+=1
    print(c)        
