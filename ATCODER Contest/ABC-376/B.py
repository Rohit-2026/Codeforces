n,q =map(int,input().split())
l=1
r=2
for i in range(q):
    h,t=map(int,input().split())
    if h=="R":
        if t!=r:
            if (l>r and l<t):
                
    else:
        if t!=l:
