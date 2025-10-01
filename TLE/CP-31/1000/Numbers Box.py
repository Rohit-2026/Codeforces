for i in range(int(input())):
    n,m=map(int,input().split())
    t=[list(map(int,input().split())) for j in range(n)]
    cn=0
    cp=0
    cz=0
    l=[]
    for i in range(n):
        for j in range(m):
            if t[i][j]<0:
                cn+=1
            elif t[i][j]>0:
                cp+=1
            else:
                cz+=1  
            l.append(abs(t[i][j])) 
    if cn%2==0:
        print(sum(l))
    elif cz>0:
        print(sum(l))
    else:
        l.sort()
        print(sum(l)-2*l[0])