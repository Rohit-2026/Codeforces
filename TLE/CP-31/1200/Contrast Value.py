for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    l=[a[0]]
    for i in range(1,n):
        if a[i]!=a[i-1]:
            l.append(a[i])
    n=len(l)
    for i in range(1,n-1):
        if l[i]>l[i-1] and l[i+1]>l[i]:
            c+=1
        elif l[i]<l[i-1] and l[i+1]<l[i]:
            c+=1   
    print(n-c)        