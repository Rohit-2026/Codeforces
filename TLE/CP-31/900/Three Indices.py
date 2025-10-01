for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=0
    l=0
    for j in range(1,n-1):
        for k in range(0,j):
            if a[k]<a[j]:
                f=1
                break
        if f==1:
            for p in range(j+1,n):
                if a[j]>a[p]:
                    l=1
                    break
        if l==1:
            print("YES")
            print(k+1,j+1,p+1)
            break
    else:
        print("NO")        

