for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    s=0
    if d<b:
        print(-1)
    else:
        s+=d-b
        a+=s
        if a<c:
            print(-1)
        else:
            s+=abs(c-a)
            print(s)