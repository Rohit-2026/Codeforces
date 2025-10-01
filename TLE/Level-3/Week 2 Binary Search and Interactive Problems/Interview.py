import sys
for i in range(int(input())):
    sys.stdout.flush()
    n=int(input())
    sys.stdout.flush()
    a=list(map(int,input().split()))
    sys.stdout.flush()
    for i in range(1,n):
        a[i]=a[i]+a[i-1]
    l=0
    h=n-1
    while l<h:
        m=(l+h)//2
        print("?",m+1,*(i for i in range(1,m+2)))
        sys.stdout.flush()
        j=int(input())
        sys.stdout.flush()
        if j<=a[m]:
            l=m+1
        else:
            h=m
        if l==h:
            break    
    print("!",l+1)
    sys.stdout.flush()    



