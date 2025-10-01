for i in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    t=sum(a)
    for i in range(1,n):
        a[i]+=a[i-1]
    for i in range(q):
        l,r,k=map(int,input().split())
        if(a[-1]-a[r-1]+(a[l-2]if l>1 else 0)+k*(r-l+1))%2==1:
            print("YES")
        else:
            print("NO")    

