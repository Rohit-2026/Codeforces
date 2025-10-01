m=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
for i in range(1,m):
    a[i]+=a[i-1]
for i in range(n):
    l=0
    h=m-1
    if b[i]<=a[0]:
        print(1)
        continue
    elif b[i]>a[-2]:
        print(m)
        continue    
    while l<h:
        mid=(h+l)//2
        if b[i]<=a[mid]:
            if b[i]>a[mid-1]:
                print(mid+1)
                break
            else:
                h=mid
        elif b[i]>=a[mid]:
            if b[i]<a[mid-1]:
                print(mid+2)
                break
            else:
                l=mid
                

