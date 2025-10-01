for i in range(int(input())):
    n,x,y=map(int,input().split())
    xc=0
    yc=0
    for i in range(1,n+1):
        if i%x==0 and i%y!=0:
            xc+=1
        elif i%y==0 and i%x!=0:
            yc+=1
    t=xc//2*(n+n-xc)-yc//2*(1+yc)
    print(t)
