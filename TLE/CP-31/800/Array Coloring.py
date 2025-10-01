for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    t=sum(a)
    k=0
    for i in a:
        if i%2==(t-i)%2:
            print("YES")
            k=1
            break
    if k==0:
        print("NO")    