for i in range(int(input())):
    n,m=map(int,input().split())
    x=input()
    s=input()
    c=0
    if s==x or s in x:
        print(0)
        continue
    while s not in x:
        if len(x)>50:
            print(-1)
            break
        else:
            x+=x
            c+=1
            if s in x:
                print(c)
                break
