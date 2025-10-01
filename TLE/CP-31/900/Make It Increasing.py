for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    if (1 in a and a.index(1) != 0) or (0 in a and a.index(0) != 0):
        print(-1)
        continue
    for i in range(n-1,0,-1):
        if a[i-1]>=a[i]:
            while a[i-1]>=a[i] and a[i - 1] > 0:
                a[i-1]//=2
                c+=1
    for i in range(1,n):
        if a[i]<a[i-1]:
            print("-1")
            break
    else:
        print(c)    
