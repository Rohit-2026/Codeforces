h,w=map(int,input().split())
s=[input().strip() for i in range(h)]
r1,r2,c1,c2=h,-1,w,-1
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            r1=min(r1,i)
            r2=max(r2,i)
            c1=min(c1,j)
            c2=max(c2,j)
for i in range(r1,r2+1):
    for j in range(c1,c2+1):
        if s[i][j]=='.':
            print("No")
            exit()
for i in range(h):
    for j in range(w):
        if i<r1 or i>r2 or j<c1 or j>c2:
            if s[i][j]=='#':
                print("No")
                exit()
print("Yes")
