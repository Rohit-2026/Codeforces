n,k=map(int,input().split())
a=list(map(int,input().split()))
b=a*2
l=0
s=0
k=k%sum(a)
if min(a)>k:
    print("No")
else:
    for r in range((n*2)-1):
        s+=b[r]
        while s>k and l<=r:
            s-=b[l]
            l+=1
        if s==k:
            print("Yes")
            break
    else:
        print("No")
