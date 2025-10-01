import math
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=0
    a.sort()
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(a[i],a[j])<=2:
                f=1
                break
        if f==1:
            break    
    if f==1:
        print("Yes")
    else:
        print("No")        
