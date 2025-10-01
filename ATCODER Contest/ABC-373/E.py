n,m,k=map(int,input().split())
a=list(map(int,input().split()))
t=k-sum(a)
l=sorted(a)
p=[]
for i in a:
    if i>l[-m]:
        p.append(0)
    elif i+t<=l[-m]:
        p.append(-1)
    elif i==l[-m]:
        o=t-l[-m]+l[-m-1]
        if o%2==0:
            p.append(o//2)
        else:
            p.append(o//2+1)        
    else:
        j=(l[-m]-i)
        if (t-j)%2==0:
            p.append(j+(t-j)//2)
        else:
            p.append(j+(t-j)//2+1)    
print(*p)
