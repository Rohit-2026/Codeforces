for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=a.count(2)
    c=0
    k=0
    if t%2==1:
        print(-1)
    else:
        for i in range(n):
            if a[i]==2:
                c+=1
            if c==t//2:
                print(i+1)
                k=1
                break    


