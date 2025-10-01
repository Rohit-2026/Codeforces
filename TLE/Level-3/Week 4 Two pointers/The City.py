n,r=map(int,input().split())
a=list(map(int,input().split()))
i=0
j=1
c=0
while j<len(a):
    if a[j]-a[i]>r:
        c+=n-j
        i+=1
    else:
        j+=1
print(c)            