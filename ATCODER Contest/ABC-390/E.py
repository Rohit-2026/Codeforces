n,x=map(int,input().split())
f=[tuple(map(int,input().split()))for _ in range(n)]
ma=0
for v,a,ca in f:ma=max(ma,a)
l,r=0,ma
an=0
while l<=r:
    m=(l+r)//2
    dp=[[-1]*(x+1)for _ in range(x+1)]
    dp[0][0]=0
    for v,a,ca in f:
        if a>=m:
            ndp=[row[:]for row in dp]
            for v1 in range(x+1):
                for v2 in range(x+1):
                    if dp[v1][v2]!=-1:
                        nv1=min(v1+(a if v==1 else 0),x)
                        nv2=min(v2+(a if v==2 else 0),x)
                        nv3=dp[v1][v2]+(a if v==3 else 0)
                        if nv3<=x:
                            ndp[nv1][nv2]=max(ndp[nv1][nv2],nv3)
            dp=ndp
    ch=False
    for v1 in range(x+1):
        for v2 in range(x+1):
            if dp[v1][v2]!=-1 and v1>=m and v2>=m and dp[v1][v2]>=m and v1+v2+dp[v1][v2]<=x:
                ch=True
                break
        if ch:break
    if ch:an=m;l=m+1
    else:r=m-1
print(an)