for i in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    t=[]
    t.append(a[0])
    t.append(2*(x-a[-1]))
    for i in range(1,n):
        t.append(a[i]-a[i-1])
    print(max(t))    