for p in range(int(input())):
    n=int(input())
    s=input()
    s=list(s)
    t=[]
    c=0
    for i in range(n):
        if s[i]==".":
            c+=1    
        else:
            if c!=0:
                t.append(c)
                c=0
    if c!=0:
        t.append(c)        
    k=0
    g=0
    for i in t:
        if i==1:
            g+=1
        elif i==2:
            g+=2
        else:
            k+=2
    if k>0:
        print(2)
    else:
        print(g)                          