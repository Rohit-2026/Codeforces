n=int(input())
a=list(map(int,input().split()))
i=0
j=0
d={}
l=10000000
if len(set(a))==n:
    print(-1)
else:
    while j<n:
        if a[j] in d:
            d[a[j]]+=1
        else:
            d[a[j]]=1
        if d[a[j]]>1:
            while d[a[j]]>1 and i<=j:
                l=min(l,j-i+1)
                d[a[i]]-=1
                i+=1
        j+=1    
    print(l)
