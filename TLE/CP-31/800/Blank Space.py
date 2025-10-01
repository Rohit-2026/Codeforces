for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    m=0
    for i in a:
        if i==1:
            c=0
        else:
            c+=1
            m=max(m,c)
    print(m)        
