for i in range(int(input())):
    n,k,d=map(int,input().split())
    a=list(map(int,input().split()))
    i=0
    j=0
    t={}
    m=1000000000000
    while i<n and j<n:
        if a[j] not in t:
            t[a[j]]=1
        else:
            t[a[j]]+=1
        while j-i+1>=d:
            m=min(m,len(t))
            if a[i] in t:
                t[a[i]]-=1
                if t[a[i]]==0:
                    del t[a[i]]    
            i+=1
        j+=1
    print(m)            


