a=list(map(int,input().split()))
c={}
for x in a:
    c[x]=c.get(x,0)+1
for v in c.values():
    if v>=3:
        for w in c.values():
            if w>=2 and v!=w:
                print("Yes")
                exit()
print("No")
