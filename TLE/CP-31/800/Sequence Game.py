for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=[a[0]]
    for i in range(1,n):
        if a[i]<a[i-1]:
            t.append(a[i])
            t.append(a[i])
        else:
            t.append(a[i])
    print(len(t))
    print(*t)            
