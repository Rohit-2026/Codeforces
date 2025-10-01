a,b,c,d,e=map(int,input().split())
p=[]
for m in range(1,32):
    n="";s=0
    if m&1:
        n+="A"
        s+=a
    if m&2:
        n+="B"
        s+=b
    if m&4:
        n+="C"
        s+=c
    if m&8:
        n+="D"
        s+=d
    if m&16:
        n+="E"
        s+=e
    p.append((s,n))
#lambda Function used from ai    
p.sort(key=lambda x:(-x[0],x[1]))
for i,n in p:
    print(n)
