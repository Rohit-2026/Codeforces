import math
for i in range(int(input())):
    n,k=map(int,input().split())
    if n%2==0:
        if k==n:
            print(n)
        elif k<=n:
            print(k)
        else:
            print(k%n)    
    else:
             