k=[]
for i in range(1,999999):
    t=len(str(i))
    if i/(10**(t-1))==i//(10**(t-1)):
        k.append(i)       
for i in range(int(input())):
    n=int(input())
    c=0
    for i in k:
        if i<=n:
            c+=1
        else:
            break
    print(c)        


