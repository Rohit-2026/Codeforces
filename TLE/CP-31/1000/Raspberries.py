for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=10000000000000
    c=0
    if k==4:
        for i in range(n):
            if a[i]%k==0:
                m=0
                break
            elif a[i]%2==0:
                c+=1
            else:
                m=min(m,k-a[i]%k)
        if m==0:
            print(0)
        elif c==0:
            print(min(2,m))
        elif c==1:
            print(1)
        else:
            print(0)            
        continue        
    for i in range(n):
        if a[i]%k==0:
            m=0
        else:
            m=min(m,k-a[i]%k)
    print(m)    