for i in range(int(input())):
    a,b=map(int,input().split())
    c=0
    k=100000000
    if b>a:
        print(1)
        continue
    elif b==a:
        print(2)
    else:
        for i in range(b,b+6):
            if i==1:
                continue
            c=i-b
            t=a
            while t:
                t//=i
                c+=1
            k=min(k,c)    
        print(k)                    
