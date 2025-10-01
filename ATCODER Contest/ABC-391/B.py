n,m=map(int,input().split())
s=[input().strip() for i in range(n)]
t=[input().strip() for i in range(m)]
for x in range(n-m+1):
    for y in range(n-m+1):
        f=1
        for i in range(m):
            for j in range(m):
                if s[x+i][y+j]!=t[i][j]:
                    f=0
                    break
            if not f:
                break
        if f:
            print(x+1,y+1)
            exit()
