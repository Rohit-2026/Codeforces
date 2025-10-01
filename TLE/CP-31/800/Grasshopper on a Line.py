for i in range(int(input())):
    n,k=map(int,input().split())
    if n%k!=0:
        print(1)
        print(n)
    else:
        print(2)
        if k%2==0:
            print(3,n-3)
        else:
            print(2,n-2)        
            