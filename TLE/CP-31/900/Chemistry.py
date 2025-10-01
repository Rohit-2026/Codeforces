for i in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    t=[]
    for i in d:
        if d[i]%2==1:
            t.append(d[i])
    if k>=len(t)-1:
        print("YES")
    else:
        print("NO")        


