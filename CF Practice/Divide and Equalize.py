def div_map(t):
    m = {}
    while t!=1:
        for i in range(2,t//2):
            while t%i==0:
                if i in m:
                    m[i]+=1
                else:
                    m[i]=1    
    return m
for p in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t=1
    for i in a:
        t*=i
    t=div_map(t)
    for i in m:
        if m[i]%n!=0:
            print("NO")
            break
    else:
        print("YES")
