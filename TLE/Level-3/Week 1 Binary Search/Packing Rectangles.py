w,r,n=map(int,input().split())
l=0
h=10**18
a=0
while l<=h:
    m=(h+l)//2
    if (m//r)*(m//w)>=n:
        a=m
        h=m-1
    else:
        l=m+1   
print(a)            
