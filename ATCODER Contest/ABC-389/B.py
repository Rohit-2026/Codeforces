x=int(input())
l,h=1,x
while l<=h:
    m=(l+h)//2
    r=1
    for i in range(1,m+1):
        r*=i
        if r>x:
            break
    if r==x:
        print(m)
        break
    elif r>x:
        h=m-1
    else:
        l=m+1
